class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        # Chuyển "J" thành "I" trong khóa và chuyển thành chữ hoa
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        # Lấy các chữ cái còn lại trong bảng chữ cái không có trong key
        remaining_letters = [letter for letter in alphabet if letter not in key_set]
        matrix = list(key)

        # Thêm các chữ cái còn lại vào ma trận
        for letter in remaining_letters:
            if letter not in matrix:  # Tránh trùng lặp
                matrix.append(letter)
            if len(matrix) == 25:
                break

        # Tạo ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None  # Trường hợp không tìm thấy (không nên xảy ra)

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" và chuyển thành chữ hoa
        plain_text = plain_text.replace("J", "I").upper()
        # Xử lý các cặp ký tự giống nhau bằng cách chèn 'X'
        processed_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i + 1]:
                    processed_text += plain_text[i] + "X"
                    i += 1
                else:
                    processed_text += plain_text[i] + plain_text[i + 1]
                    i += 2
            else:
                processed_text += plain_text[i] + "X"
                i += 1

        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            pair = processed_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Cùng hàng: dịch phải 1 cột
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                # Cùng cột: dịch xuống 1 hàng
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                # Hình chữ nhật: lấy góc đối diện
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        # Chuyển thành chữ hoa
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                # Cùng hàng: dịch trái 1 cột
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                # Cùng cột: dịch lên 1 hàng
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                # Hình chữ nhật: lấy góc đối diện
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        # Loại bỏ ký tự 'X' được thêm vào trong quá trình mã hóa
        result = ""
        i = 0
        while i < len(decrypted_text):
            if i + 1 < len(decrypted_text) and decrypted_text[i + 1] == 'X':
                result += decrypted_text[i]
                i += 2
            else:
                result += decrypted_text[i]
                i += 1

        return result