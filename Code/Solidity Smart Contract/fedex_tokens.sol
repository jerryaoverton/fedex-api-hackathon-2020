pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";

contract FedexToken is ERC20, ERC20Detailed {

    constructor () public ERC20Detailed("Fedex Token", "TKX", 1) {
        _mint(msg.sender, 1000000);
    }
}