"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
TESTS = {
    "Basics": [
        {
            "input": [6, 4],
            "answer": 2
        },
        {
            "input": [2, 4, 8],
            "answer": 2
        },
        {
            "input": [2, 3, 5, 7, 11],
            "answer": 1
        },
        {
            "input": [3, 9, 3, 9],
            "answer": 3
        },
    ],
    "Edge": [
        {
            "input": [1, 1],
            "answer": 1
        },
        {
            "input": [4294967296, 2],
            "answer": 2
        },
        {
            "input": [32, 256, 2048, 16384, 131072, 1048576, 8388608, 67108864, 536870912, 4294967296],
            "answer": 32
        },
        {
            "input": [11, 13, 17, 19, 23, 29, 31, 37, 41, 43],
            "answer": 1
        },
        {
            "input": [6, 10, 15],
            "answer": 1
        },
        {
            "input": [210, 330, 462, 770],
            "answer": 2
        },
        {
            "input": [180, 300, 450],
            "answer": 30
        },

    ],
    "Extra": [
        {
            "input": [2226172404, 2652430846, 3702223254, 3260139372, 2021191608],
            "answer": 2
        },
        {
            "input": [1047734205, 731227527],
            "answer": 3
        },
        {
            "input": [606914679, 1496978895, 3951290184],
            "answer": 3
        },
        {
            "input": [1540765093, 1353759337, 1120458213],
            "answer": 7
        },
        {
            "input": [2655680644, 2383739556, 3860750380, 1756514556],
            "answer": 4
        },
        {
            "input": [2167650657, 1496767446, 2685881265, 452884638, 2222724963],
            "answer": 3
        },
    ]
}
