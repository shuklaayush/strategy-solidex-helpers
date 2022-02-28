## Ideally, they have one file with the settings for the strat and deployment
## This file would allow them to configure so they can test, deploy and interact with the strategy
from dotmap import DotMap

BADGER_DEV_MULTISIG = "0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b"

sett_config = DotMap(
    helpers = DotMap(
        sexWftmLp = DotMap(
            WANT = "0xFCEC86aF8774d69e2e4412B8De3f4aBf1f671ecC",  ## wFTM/SEX LP
            LP_COMPONENT =  "0xD31Fcd1f7Ba190dBc75354046F6024A9b86014d7",  ## SEX
            REWARD_TOKEN = "0x888ef71766ca594ded1f0fa3ae64ed2941740a20",  ## SOLID
            WHALE = "0x0d1e161ef65e5981ea0fe673bcf359c46f2364aa"
        ),
        solidSolidsexLp = DotMap(
            WANT = "0x62E2819Dd417F3b430B6fa5Fd34a49A377A02ac8",  ## SOLID/SOLIDsex LP
            LP_COMPONENT =  "0x888ef71766ca594ded1f0fa3ae64ed2941740a20",  ## SOLID
            REWARD_TOKEN = "0xD31Fcd1f7Ba190dBc75354046F6024A9b86014d7",  ## SEX
            WHALE = "0x39de56518e136d472ef9645e7d6e1f7c6c8ed37b"
        )
    )
)

# Wants
SEX_WFTM_LP = "0xFCEC86aF8774d69e2e4412B8De3f4aBf1f671ecC"
SOLID_SOLIDSEX_LP = "0x62E2819Dd417F3b430B6fa5Fd34a49A377A02ac8"

## Fees in Basis Points
DEFAULT_GOV_PERFORMANCE_FEE = 1500
DEFAULT_PERFORMANCE_FEE = 0
DEFAULT_WITHDRAWAL_FEE = 10

FEES = [DEFAULT_GOV_PERFORMANCE_FEE, DEFAULT_PERFORMANCE_FEE, DEFAULT_WITHDRAWAL_FEE]

BADGER_TREE = "0x89122c767A5F543e663DB536b603123225bc3823"

REGISTRY = "0xFda7eB6f8b7a9e9fCFd348042ae675d1d652454f"  # Multichain BadgerRegistry
