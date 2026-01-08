import pytest
from market_sim.blockchain.consensus.bft_consensus import BFTConsensus

def test_bft_agreement():
    """Verifies that consensus is reached even with a malicious node."""
    consensus_engine = BFTConsensus(node_id="Master", total_nodes=4)
    trade_id = "TX_99"

    consensus_engine.receive_vote(trade_id, "Node_1", 100.0)
    consensus_engine.receive_vote(trade_id, "Node_2", 100.0)
    consensus_engine.receive_vote(trade_id, "Node_3", 100.0)

    consensus_engine.receive_vote(trade_id, "Node_4", 500.0)

    assert consensus_engine.verify_consensus(trade_id) is True