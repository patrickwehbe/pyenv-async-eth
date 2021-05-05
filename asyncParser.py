import asyncio
from Crypto.Hash import keccak
import time


def getHash(stringToHash):
    return keccak.new(
        digest_bits=256,
        data=stringToHash.encode('utf-8')
    ).hexdigest()


async def getBlockHeader(blocknumber):
    await asyncio.sleep(0.1)
    return {
        'blocknumber': blocknumber,
        'blockhash': getHash(str(blocknumber)),
        'transactions': [
            getHash(str(blocknumber)+str(num)) for num in range(10)
        ]
    }


async def getTransactionReceipt(txHash):
    # Returns fake transaction receipt
    await asyncio.sleep(0.1)
    return getHash(txHash)


async def parseBlocks(blocksToFetch):

    ''' Fetches batch of block headers and transaction receipts.
    Return data in the following format:
    [
        [
            blockheader,
            txReceiptDict: {
                txHash: data,
                ...
            }
        ],
        ...
    ]
    '''
    # Complete this function
    blockData = []
    txReceiptDict = {}

    for blockNumber in blocksToFetch:
        blockData.append([])
        blockHeader = await getBlockHeader(blockNumber)        
        blockData[blockNumber].append(blockHeader)
        for transaction in blockHeader["transactions"]:
            txReceiptDict[transaction] = await getTransactionReceipt(transaction)
            blockData[blockNumber].append(txReceiptDict)
    print(blockData)       
    return blockData


def main():
    loop = asyncio.get_event_loop()
    blocksToFetch = range(5)
    # Fetch blocks and transaction receipts
    startTime = time.time()
    blockData = loop.run_until_complete(parseBlocks(blocksToFetch))
    # Test results
    assert len(blockData) == 5
    for block in blockData:
        assert block[0]['blockhash'] == getHash(str(block[0]['blocknumber']))
        assert len(block[0]['transactions']) == 10
        assert isinstance(block[1], dict)
        for txHash in block[1]:
            assert block[1][txHash] == getHash(txHash)
    print('Passed!')
    print(time.time() - startTime)


if __name__ == "__main__":
    main()
