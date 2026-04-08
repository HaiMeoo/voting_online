// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {

    // lưu số phiếu theo tên ứng viên
    mapping(string => uint256) public votes;

    // kiểm tra đã vote chưa
    mapping(address => bool) public hasVoted;

    // danh sách ứng viên (optional)
    string[] public candidates;

    // constructor
    constructor(string[] memory _candidates) {
        candidates = _candidates;
    }

    // vote
    function vote(string memory name) public {
        require(!hasVoted[msg.sender], "Ban da vote roi!");

        votes[name] += 1;
        hasVoted[msg.sender] = true;
    }

    // lấy số phiếu
    function getVotes(string memory name) public view returns (uint256) {
        return votes[name];
    }

    // lấy danh sách ứng viên
    function getCandidates() public view returns (string[] memory) {
        return candidates;
    }
}