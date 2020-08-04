pragma solidity >=0.4.22 <0.7.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.
import "../fedex_token_network.sol";
import "../fedex_tokens.sol";

// File name has to end with '_test.sol', this file can contain more than one testSuite contracts
contract testSuite {
    
    // Create the currency and network
    address token_addr = 0xbf50152A106e028e09D4b971011CC81F333d8b3b;
    address network_addr = 0xcd2daB71534dC8287dF20Fe6420906dAFf8a869a;
    
    // The token network members
    address fedex = address(this);
    address drone = 0xb6eEC5F4CB27897711Fe927B05513Bdcf42111f2;
    address ann_the_pizza_shop_owner = 0xe21F3B42DAaEFf2be18224a5236ABC5C702Bf92E;
    address bob_the_drone_tech = 0x34B95B86a0bE3E398055BA3563a877262572aF8a;
    address tina_the_microsoft_exec = 0x8c69216680f6DC408f571DC6b77CEC9EC350a51A;
    
    // The Fedex token network
    FedexToken token = new FedexToken();
    FedexTokenNetwork network = FedexTokenNetwork(network_addr);

    /// 'beforeAll' runs before all other tests
    /// More special functions are: 'beforeEach', 'beforeAll', 'afterEach' & 'afterAll'
    function beforeAll() public {
        network.set_token_address(address(token));
    }

    function checkFundMembers() public {
        uint inital_token_balance = token.balanceOf(ann_the_pizza_shop_owner);
        uint seed_investment = uint(500);
        
        // provide the small business with seed funding
        token.approve(network_addr, seed_investment);
        network.pay(ann_the_pizza_shop_owner, seed_investment);
        
        uint expected_balance = inital_token_balance + seed_investment;
        Assert.equal(token.balanceOf(ann_the_pizza_shop_owner), expected_balance, "Seed funding was not paid");
    }

}
