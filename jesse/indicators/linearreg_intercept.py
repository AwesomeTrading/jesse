from typing import Union

import numpy as np
import talib

from jesse.helpers import get_candle_source
from jesse.helpers import slice_candles


def linearreg_intercept(candles: np.ndarray, period: int = 14, source_type: str = "close", sequential: bool = False) -> \
        Union[float, np.ndarray]:
    """
    LINEARREG_INTERCEPT - Linear Regression Intercept

    :param candles: np.ndarray
    :param period: int - default: 14
    :param source_type: str - default: "close"
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    candles = slice_candles(candles, sequential)

    source = get_candle_source(candles, source_type=source_type)
    res = talib.LINEARREG_INTERCEPT(source, timeperiod=period)

    return res if sequential else res[-1]
