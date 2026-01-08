import hashlib
from typing import Dict, Any

class BFTConsensus:
    
    def __init__(self, node_id: str, total_nodes: int):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.threshold = (2 * (total_nodes // 3)) + 1 
        self.votes: Dict[str, Dict[str, float]] = {} 

    def receive_vote(self, trade_id: str, voter_id: str, price: float):
        
        if trade_id not in self.votes:
            self.votes[trade_id] = {}
        self.votes[trade_id][voter_id] = price

    def verify_consensus(self, trade_id: str) -> bool:
        if trade_id not in self.votes:
            return False
        
        price_counts = {}
        for price in self.votes[trade_id].values():
            price_counts[price] = price_counts.get(price, 0) + 1
            
        for price, count in price_counts.items():
            if count >= self.threshold:
                return True
        return False