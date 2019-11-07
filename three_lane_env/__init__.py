from gym.envs.registration import register

register(
    id='three-lane-env-v0',
    entry_point='three_lane_env.envs:ThreeLaneEnv',
)