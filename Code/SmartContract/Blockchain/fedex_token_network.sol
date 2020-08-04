pragma solidity >=0.4.22 <0.6.0;

import "./fedex_tokens.sol";

contract FedexTokenNetwork {
    
    //state
    mapping(address => string) _user_profiles;
    address[] _user_list;
    address _fedex_token_address;
    
    //functions
    function set_token_address(address fedex_token_address) external {
        _fedex_token_address = fedex_token_address;
    }
    
    function register_user(string memory profile) public{
        address sender = msg.sender;
        _user_profiles[sender] = profile;
        _user_list.push(sender);
    }
    
    function update_profile(string memory profile) public{
        address sender = msg.sender;
        _user_profiles[sender] = profile;
        emit profile_change(profile);
    }
    
    function users() public view returns (address[] memory){
        return _user_list;
    }
    
    function user_profile(address user) public view returns (string memory){
        return _user_profiles[user];
    }
    
    function update_order(string memory order) public{
        emit order_change(order);
    }
    
    function pay(address payee, uint amount) external payable{
        FedexToken token = FedexToken(_fedex_token_address);
        address sender = msg.sender;
        token.transferFrom(sender, payee, amount);
    }
    
    //notifications
    event profile_change(string profile);
    event order_change(string order);
}