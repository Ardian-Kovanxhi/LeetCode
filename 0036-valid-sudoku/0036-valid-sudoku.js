/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const column = {};
    const row = {};
    const square = {};

    let res

    for (let y = 0; y < board.length; y++) {
        row[y] = {}
        for (let x = 0; x < board.length; x++) {
            const curr = board[y][x];
            const coord = [Math.floor(x/3), Math.floor(y/3)];

            if (!column[x]) column[x] = {}
            if (!square[coord]) square[coord] = {}
            
            if (curr !== '.') {
                if (row[y][curr] || column[x][curr] || square[coord][curr]) return false
                row[y][curr] = true
                column[x][curr] = true
                square[coord][curr] = true
            }
        }
    }
    return true
};