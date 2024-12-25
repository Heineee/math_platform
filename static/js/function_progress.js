document.addEventListener('DOMContentLoaded', () => {
    const operationSelect = document.getElementById('operationSelect');
    const integralInputs = document.getElementById('integralInputs');
    const derivativeInputs = document.getElementById('derivativeInputs');
    const calculateButton = document.getElementById('calculateButton');
    const resultOutput = document.getElementById('resultOutput');

    // 复化 Simpson 公式积分计算
    function compositeSimpson(f, a, b, n) {
        const h = (b - a) / n;
        let sum = f(a) + f(b);

        for (let i = 1; i < n; i += 2) {
            sum += 4 * f(a + i * h);
        }
        for (let i = 2; i < n; i += 2) {
            sum += 2 * f(a + i * h);
        }
        return (h / 3) * sum;
    }

    // 数值方法计算导数
    function numericDerivative(f, x0, epsilon = 1e-6) {
        const h = epsilon;
        return (f(x0 + h) - f(x0 - h)) / (2 * h);
    }

    // 显示或隐藏积分、导数的输入框
    function updateInputs() {
        const selectedOperation = operationSelect.value;
        integralInputs.classList.toggle('hidden', selectedOperation !== 'integral');
        derivativeInputs.classList.toggle('hidden', selectedOperation !== 'derivative');
    }

    // 默认选中积分功能
    operationSelect.value = 'integral';
    updateInputs();

    // 监听功能选择变化
    operationSelect.addEventListener('change', updateInputs);

    // 点击计算按钮时触发
    calculateButton.addEventListener('click', () => {
        const functionInput = document.getElementById('functionInput').value;
        const lowerLimit = parseFloat(document.getElementById('lowerLimit').value);
        const upperLimit = parseFloat(document.getElementById('upperLimit').value);
        const derivativePoint = parseFloat(document.getElementById('derivativePoint').value);
        let result = '';

        try {
            // 解析函数并编译
            const parsedFunction = math.compile(functionInput);

            // 创建函数评估器
            const func = x => parsedFunction.evaluate({ x });

            const selectedOperation = operationSelect.value;
            if (selectedOperation === 'integral') {
                // 积分功能
                if (isNaN(lowerLimit) || isNaN(upperLimit)) {
                    result = '请输入有效的积分上下限';
                } else {
                    // 计算积分
                    const integralResult = compositeSimpson(func, lowerLimit, upperLimit, 1000);
                    result = `计算结果：${functionInput} 在 [${lowerLimit}, ${upperLimit}] 区间的积分结果为: ${integralResult.toFixed(5)}`;
                }

            } else if (selectedOperation === 'derivative') {
                // 导数功能
                if (isNaN(derivativePoint)) {
                    result = '请输入有效的导数计算点';
                } else {
                    // 计算导数
                    const derivativeResult = numericDerivative(func, derivativePoint);
                    result = `计算结果：${functionInput} 在 x = ${derivativePoint} 处的导数值为: ${derivativeResult.toFixed(5)}`;
                }
            }

        } catch (error) {
            result = '计算错误，请检查输入的函数或格式是否正确';
        }

        // 输出计算结果
        resultOutput.value = result;
    });
});
