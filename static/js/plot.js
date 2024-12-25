// script.js
function plotFunction() {
    const canvas = document.getElementById('plotCanvas');
    const ctx = canvas.getContext('2d');
    const functionInput = document.getElementById('functionInput').value;

    // Set canvas size
    canvas.width = 800;
    canvas.height = 600;

    // Clear previous drawing
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Create function from input
    const func = new Function('x', `return ${latexToJavaScript(functionInput)}`);

    // Set plotting range
    const scale = 40; // Pixels per unit
    const minX = -canvas.width / (2 * scale);
    const maxX = canvas.width / (2 * scale);
    const minY = -canvas.height / (2 * scale);
    const maxY = canvas.height / (2 * scale);

    // Draw axes
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 2;

    const offsetX = canvas.width / 2;
    const offsetY = canvas.height / 2;

    // Draw x-axis
    ctx.beginPath();
    ctx.moveTo(0, offsetY);
    ctx.lineTo(canvas.width, offsetY);
    ctx.stroke();

    // Draw y-axis
    ctx.beginPath();
    ctx.moveTo(offsetX, 0);
    ctx.lineTo(offsetX, canvas.height);
    ctx.stroke();

    // Draw axis arrows
    function drawArrow(fromX, fromY, toX, toY) {
        const headLength = 10; // Length of the arrow head
        const angle = Math.atan2(toY - fromY, toX - fromX);

        ctx.beginPath();
        ctx.moveTo(toX, toY);
        ctx.lineTo(toX - headLength * Math.cos(angle - Math.PI / 6), toY - headLength * Math.sin(angle - Math.PI / 6));
        ctx.lineTo(toX - headLength * Math.cos(angle + Math.PI / 6), toY - headLength * Math.sin(angle + Math.PI / 6));
        ctx.lineTo(toX, toY);
        ctx.stroke();
        ctx.fillStyle = '#000';
        ctx.fill();
    }

    // Draw x-axis arrow
    drawArrow(offsetX, offsetY, canvas.width - 30, offsetY);

    // Draw y-axis arrow
    drawArrow(offsetX, offsetY, offsetX, 30);

    // Draw axis labels
    ctx.fillStyle = '#000';
    ctx.font = '16px Arial';
    ctx.textAlign = 'center';

    // x-axis label
    ctx.fillText('x', canvas.width - 30, offsetY - 10);

    // y-axis label
    ctx.save();
    ctx.translate(offsetX - 20, 30);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('y', 0, 0);
    ctx.restore();

    // Draw function
    ctx.strokeStyle = '#ff0000';
    ctx.lineWidth = 2;
    ctx.beginPath();

    let prevX = null;
    let prevY = null;

    for (let x = -canvas.width / 2; x < canvas.width / 2; x++) {
        const xCoord = x / scale;
        let yCoord;

        try {
            yCoord = func(xCoord);
            if (isNaN(yCoord) || !isFinite(yCoord)) {
                continue; // Skip invalid values
            }
        } catch (e) {
            console.error(e);
            continue;
        }

        const xPixel = offsetX + x;
        const yPixel = offsetY - yCoord * scale;

        if (prevX !== null && prevY !== null) {
            ctx.lineTo(xPixel, yPixel);
        } else {
            ctx.moveTo(xPixel, yPixel);
        }

        prevX = xPixel;
        prevY = yPixel;
    }

    ctx.stroke();
}

function latexToJavaScript(latex) {
    // Basic LaTeX to JavaScript conversion
    let js = latex
        .replace(/\\sin/g, 'Math.sin')
        .replace(/\\cos/g, 'Math.cos')
        .replace(/\\tan/g, 'Math.tan')
        .replace(/\\exp/g, 'Math.exp')
        .replace(/\\log/g, 'Math.log')
        .replace(/\\sqrt\{(.+?)\}/g, 'Math.sqrt($1)')
        .replace(/\\left\(/g, '(')
        .replace(/\\right\)/g, ')')
        .replace(/\\cdot/g, '*')
        .replace(/([a-zA-Z])\^(\d+(\.\d+)?)/g, 'Math.pow($1, $2)') // Handle x^a and x^0.2
        .replace(/([0-9]+(?:\.[0-9]+)?)\s*\/\s*([0-9]+(?:\.[0-9]+)?)/g, '($1) / ($2)') // Handle division
        .replace(/x/g, 'x')
        .replace(/([0-9])/g, '$1') // Handle numbers
        .replace(/\\frac\{(.+?)\}\{(.+?)\}/g, '($1) / ($2)') // Handle fractions
        .replace(/^\s*\(\s*/g, '(') // Handle extra spaces around parentheses
        .replace(/\s*\)\s*$/g, ')') // Handle extra spaces around parentheses
        .replace(/\\sin\((x)\)\^2/g, 'Math.pow(Math.sin($1), 2)') // Handle sin(x)^2
        .replace(/\\cos\((x)\)\^2/g, 'Math.pow(Math.cos($1), 2)') // Handle cos(x)^2
        .replace(/\\tan\((x)\)\^2/g, 'Math.pow(Math.tan($1), 2)') // Handle tan(x)^2
        .replace(/([a-zA-Z])\^0\.5/g, 'Math.sqrt($1)') // Handle x^0.5
        .replace(/([a-zA-Z])\^0\.(\d+)/g, 'Math.pow($1, 0.$2)'); // Handle x^0.1, x^0.01, etc.

    return js;
}
