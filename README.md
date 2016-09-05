## DroneEmployee video streaming support

The aim of this is a spawn `streamer` (the executable that stream video)
according to smart contract logic. The code works with [Streaming.sol][1].

The `streamer` is any bynary with two args:

 - video device (e.g. `/dev/video0`)
 - stream identifier (256bit hex, e.g. `4f66e...`) 

[1]: https://github.com/DroneEmployee/contracts/blob/master/interface/Streaming.sol

### Usage

    $ ./bin/streamd.sh              
    Usage: /usr/bin/node ./scripts/streamd.js -c [CONTRACT_ADDRESS] -e [STREAMING_BINARY]
    
    Options:
        --rpc  Web3 RPC provider                        [default: "http://localhost:8545"]
        -d     Video device to streaming                [default: "/dev/video0"]
        -c     Streaming contract address               [required]
        -e     Shell command to start streaming daemon  [required]
