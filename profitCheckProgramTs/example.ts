import fs from "fs";
import * as anchor from '@coral-xyz/anchor';
import BN from "bn.js";
import { Keypair, PublicKey, SystemProgram } from "@solana/web3.js";
import { getAssociatedTokenAddressSync } from "@solana/spl-token";



function getPayerFromKeypairPath(keypairPath) {
  const secretKeyString = fs.readFileSync(keypairPath, 'utf8');
  const secretKey = Uint8Array.from(JSON.parse(secretKeyString));
  return Keypair.fromSecretKey(secretKey);
}

const payerKeypairPath = '/path/to/your/keypair.json';
const payer = getPayerFromKeypairPath(payerKeypairPath);

const wallet = new anchor.Wallet(payer);

const IDL = JSON.parse(
    fs.readFileSync('./ledger_program.json', 'utf-8'),
  ) as anchor.Idl;


const connection = new anchor.web3.Connection('rpc url');

const provider = new anchor.AnchorProvider(connection, wallet, {
  commitment: "confirmed",
});

const LEDGER_PROGRAM_ID = "3tZPEagumHvtgBhivFJCmhV9AyhBHGW9VgdsK52i4gwP";
const ledgerProgram = new anchor.Program(IDL, LEDGER_PROGRAM_ID, provider);

const inputMint = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"; // whatever your input mint is

const feePayerAta = getAssociatedTokenAddressSync(new PublicKey(inputMint), wallet.publicKey);
const feeReceiverAta = getAssociatedTokenAddressSync(new PublicKey(inputMint), new PublicKey("D96EFRTeN2PSxqUfiHEQyKmwHLAE39Lcq23W2v5FJi8V"));



const randomSeed = new BN(Math.floor(Math.random() * 1000000));

const ledgerAccount = PublicKey.findProgramAddressSync(
  [Buffer.from("ledgerx"), wallet.publicKey.toBuffer()],
  ledgerProgram.programId
)[0];

// Add these instructions to your transaction
// put the start instruction before your swap instruction
// put the end instruction after your swap instruction

const startLedgerIx = await ledgerProgram.methods.startLedger(randomSeed)
.accounts({
  signer: wallet.publicKey,
  monitorAta: feePayerAta,
  ledgerAccount: ledgerAccount,
  systemProgram: SystemProgram.programId,
})
.instruction();

const minProfitAsInt = Math.floor(100);
const endLedgerIx = await ledgerProgram.methods.endLedger(
    randomSeed, 
    new BN(minProfitAsInt), 
    new BN(8)) // any int between 1 and 10 inclusive
.accounts({
  signer: wallet.publicKey,
  monitorAta: feePayerAta,
  ledgerAccount: ledgerAccount,
  destinationAta: feeReceiverAta,
  tokenProgram: anchor.utils.token.TOKEN_PROGRAM_ID,
})
.instruction();