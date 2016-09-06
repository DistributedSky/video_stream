var streaming = {}; 
streaming.abi = require('./streaming_abi.js')(); 
const spawn = require('child_process').spawn;
const Web3 = require('web3');
const web3 = new Web3();

const argv = require('optimist')
    .usage('Usage: $0 -c [CONTRACT_ADDRESS] -e [STREAMING_BINARY]')
    .default({d: '/dev/video0', rpc: 'http://localhost:8545'})
    .describe('rpc', 'Web3 RPC provider')
    .describe('d', 'Video device to streaming')
    .describe('c', 'Streaming contract address')
    .describe('e', 'Shell command to start streaming daemon')
    .demand(['c', 'e'])
    .argv;

// Video process spawner
function video_process(ident)
{ return spawn(argv.e, [argv.d, ident]); }

// Connect web3
web3.setProvider(new web3.providers.HttpProvider(argv.rpc));

// Load contract
streaming.address  = argv.c.replace(/"/g, '');
streaming.contract = web3.eth.contract(streaming.abi).at(streaming.address);

// Listen Stream event
streaming.contract.Stream({}, '', (e, r) => {
    if (e) {
        console.error('Error occured:');
        console.error(e);
    } else {
        const ident = r.args.ident;
        const alive = r.args.alive;
        console.log("Incoming stream: " + {ident: ident, alive: alive});

        if (streaming.child) {
            if (streaming.child.ident != ident)
                console.warn('Override child process '
                            + streaming.child.ident + ' => ' + ident);
            // Kill the child
            streaming.child.process.kill();
        }
        if (alive)
            streaming.child = {ident: ident, process: video_process(ident)};
        else {
            streaming.child.process.kill();
            streaming.child = null;
        }
    }
});
