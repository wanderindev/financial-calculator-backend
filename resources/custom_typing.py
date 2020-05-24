from typing import Dict, List, Tuple, Union


FullResponseJSON = Tuple[
    Union[
        Dict[
            str,
            Union[int, float, List[int], List[Dict[str, Union[int, float]]]],
        ]
    ],
    int,
    str,
]
SimpleResponseJSON = Tuple[Union[Dict[str, float]], int, str]
