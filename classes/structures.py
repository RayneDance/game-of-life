

class Structures:

    @staticmethod
    def toggle_vertical(structure):
        st = structure["structure"].reverse()
        structure["structure"] = st
        return structure

    @staticmethod
    def toggle_horizontal(structure):
        st = structure["structure"]
        for i in range(len(st)):
            st[i] = st[i].reverse()
        structure["structure"] = st
        return structure

    @staticmethod
    def toggle_flip(structure):
        st = structure["structure"]
        for i in range(len(st)):
            st[i] = st[i].reverse()
        st = st.reverse()
        structure["structure"] = st
        return structure

    @staticmethod
    def glider():
        return {
            "size": (3, 3),
            "structure": [
                [0, 1, 0],
                [0, 0, 1],
                [1, 1, 1]
            ]
        }

    @staticmethod
    def blinker():
        return {
            "size": (3, 1),
            "structure": [
                [1, 1, 1]
            ]
        }

    @staticmethod
    def toad():
        return {
            "size": (4, 2),
            "structure": [
                [0, 1, 1, 1],
                [1, 1, 1, 0]
            ]
        }

    @staticmethod
    def beacon():
        return {
            "size": (4, 4),
            "structure": [
                [1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]
            ]
        }

    @staticmethod
    def pulsar():
        return {
            "size": (13, 13),
            "structure": [
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
            ]
        }
