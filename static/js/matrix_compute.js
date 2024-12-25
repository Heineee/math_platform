// 生成矩阵输入框
function generateMatrixInputs(matrixId) {
    let rows = document.getElementById(matrixId === 'matrix1' ? 'rowsMatrix1' : 'rowsMatrix2').value;
    let cols = document.getElementById(matrixId === 'matrix1' ? 'colsMatrix1' : 'colsMatrix2').value;
    let matrixContainer = document.getElementById(matrixId);
    
    matrixContainer.innerHTML = '';
    for (let i = 0; i < rows; i++) {
        let rowDiv = document.createElement('div');
        rowDiv.className = 'matrix-input';
        for (let j = 0; j < cols; j++) {
            let input = document.createElement('input');
            input.type = 'number';
            input.value = 0;
            input.id = `${matrixId}_r${i}c${j}`;
            rowDiv.appendChild(input);
        }
        matrixContainer.appendChild(rowDiv);
    }
}

// 获取输入矩阵的数据
function getMatrixData(matrixId, rows, cols) {
    let matrix = [];
    for (let i = 0; i < rows; i++) {
        let row = [];
        for (let j = 0; j < cols; j++) {
            let value = parseFloat(document.getElementById(`${matrixId}_r${i}c${j}`).value);
            row.push(value);
        }
        matrix.push(row);
    }
    return matrix;
}

// 显示矩阵结果
function displayMatrix(matrix, container) {
    container.innerHTML = '';
    matrix.forEach(row => {
        let rowDiv = document.createElement('div');
        rowDiv.className = 'matrix-input';
        row.forEach(value => {
            let output = document.createElement('input');
            output.type = 'text';
            output.value = value;
            output.disabled = true;
            rowDiv.appendChild(output);
        });
        container.appendChild(rowDiv);
    });
}

// 矩阵乘法运算
function matrixMultiply(matrix1, matrix2) {
    let result = [];
    for (let i = 0; i < matrix1.length; i++) {
        result[i] = [];
        for (let j = 0; j < matrix2[0].length; j++) {
            let sum = 0;
            for (let k = 0; k < matrix1[0].length; k++) {
                sum += matrix1[i][k] * matrix2[k][j];
            }
            result[i][j] = sum;
        }
    }
    return result;
}

// 执行选定的矩阵操作
function calculateOperation() {
    let rowsMatrix1 = parseInt(document.getElementById('rowsMatrix1').value);
    let colsMatrix1 = parseInt(document.getElementById('colsMatrix1').value);
    let rowsMatrix2 = parseInt(document.getElementById('rowsMatrix2').value);
    let colsMatrix2 = parseInt(document.getElementById('colsMatrix2').value);

    let operation = document.getElementById("operationSelector").value;

    let matrix1 = getMatrixData('matrix1', rowsMatrix1, colsMatrix1);
    let matrix2 = getMatrixData('matrix2', rowsMatrix2, colsMatrix2);

    let resultMatrixContainerL = document.getElementById('resultMatrixL');
    let resultMatrixContainerU = document.getElementById('resultMatrixU');
    let resultMatrixContainer = document.getElementById('resultMatrix'); // 用于其他运算的结果

    // 清空结果框内容
    resultMatrixContainerL.innerHTML = '';
    resultMatrixContainerU.innerHTML = '';
    resultMatrixContainer.innerHTML = '';

    try {
        let result;

        switch (operation) {
            case "product":
                if (colsMatrix1 !== rowsMatrix2) {
                    alert("Matrix multiplication is not possible. Columns of Matrix 1 must match Rows of Matrix 2.");
                    return;
                }
                result = matrixMultiply(matrix1, matrix2);
                displayMatrix(result, resultMatrixContainer);
                break;

            case "inverseLeft":
                if (rowsMatrix1 !== colsMatrix1) {
                    alert("Inverse can only be computed for square matrices.");
                    return;
                }
                result = math.inv(matrix1);
                displayMatrix(result, resultMatrixContainer);
                break;

            case "inverseRight":
                if (rowsMatrix2 !== colsMatrix2) {
                    alert("Inverse can only be computed for square matrices.");
                    return;
                }
                result = math.inv(matrix2);
                displayMatrix(result, resultMatrixContainer);
                break;

            case "eigenLeft":
                if (rowsMatrix1 !== colsMatrix1) {
                    alert("Eigenvalues can only be computed for square matrices.");
                    return;
                }
                result = math.eigs(matrix1).values;
                displayMatrix([result], resultMatrixContainer);
                break;

            case "eigenRight":
                if (rowsMatrix2 !== colsMatrix2) {
                    alert("Eigenvalues can only be computed for square matrices.");
                    return;
                }
                result = math.eigs(matrix2).values;
                displayMatrix([result], resultMatrixContainer);
                break;

            case "luLeft":
                if (rowsMatrix1 !== colsMatrix1) {
                    alert("LU decomposition can only be computed for square matrices.");
                    return;
                }
                result = math.lup(matrix1);  // LU decomposition
                displayMatrix(result.L, resultMatrixContainerL); // 显示L矩阵
                displayMatrix(result.U, resultMatrixContainerU); // 显示U矩阵
                break;

            case "luRight":
                if (rowsMatrix2 !== colsMatrix2) {
                    alert("LU decomposition can only be computed for square matrices.");
                    return;
                }
                result = math.lup(matrix2);  // LU decomposition
                displayMatrix(result.L, resultMatrixContainerL); // 显示L矩阵
                displayMatrix(result.U, resultMatrixContainerU); // 显示U矩阵
                break;

            case "qrLeft":
                if (rowsMatrix1 !== colsMatrix1) {
                    alert("QR decomposition can only be computed for square matrices.");
                    return;
                }
                result = math.qr(matrix1);  // QR decomposition
                displayMatrix(result.Q, resultMatrixContainerL); // 显示Q矩阵
                displayMatrix(result.R, resultMatrixContainerU); // 显示R矩阵
                break;

            case "qrRight":
                if (rowsMatrix2 !== colsMatrix2) {
                    alert("QR decomposition can only be computed for square matrices.");
                    return;
                }
                result = math.qr(matrix2);  // QR decomposition
                displayMatrix(result.Q, resultMatrixContainerL); // 显示Q矩阵
                displayMatrix(result.R, resultMatrixContainerU); // 显示R矩阵
                break;

            default:
                alert("Invalid operation selected.");
                break;
        }
    } catch (error) {
        alert("An error occurred during the operation: " + error.message);
    }
}




