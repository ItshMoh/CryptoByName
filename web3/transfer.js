const { ethers } = require("ethers");
const privateKey = "0d3716372d0ccc3d1b2bf1305ab23bacdc4f1af45cd889ea6eac7198e83d1d4e";
async function sendTransaction (toAddress, amount) {
  try {
    // Connect to Sapphire testnet
    const provider = new ethers.JsonRpcProvider("https://testnet.sapphire.oasis.dev");

    const wallet = new ethers.Wallet(privateKey, provider);
    const txAmount = ethers.parseEther(amount.toString());

    const tx = await wallet.sendTransaction({
      to: toAddress,
      value: txAmount
    });

    console.log(`Transaction hash: ${tx.hash}`);
    await tx.wait();
    console.log("Transaction confirmed!");

  } catch (error) {
    console.error("Transaction failed:", error);
  }
}

if (require.main === module) {
  // For command line usage
  const [,, toAddress, amount] = process.argv;
  sendTransaction(toAddress, amount);
} else {
  // For module usage
  module.exports = sendTransaction;
}
// Usage example - replace with your values

