const API_URL =
"https://hsxibhjpfrtw2snldkstn7cdwa0ggefb.lambda-url.us-east-2.on.aws/";

async function buscar() {

    let id = document.getElementById("txid").value;

    let response = await fetch(
        API_URL + "?id=" + id
    );

    let data = await response.json();

    document.getElementById("resultado").innerHTML = `
        <h3>Detalle de la Venta</h3>

        <p><b>ID:</b> ${data.TransactionID}</p>
        <p><b>Producto:</b> ${data.Item}</p>
        <p><b>Cantidad:</b> ${data.Quantity}</p>
        <p><b>Total:</b> ${data.TotalSpent}</p>
    `;
}


async function mostrarTodas() {

    let response = await fetch(API_URL);

    let datos = await response.json();

    let tabla = `
        <table border="1" style="margin:auto;">
            <tr>
                <th>ID</th>
                <th>Producto</th>
                <th>Cantidad</th>
                <th>Total</th>
            </tr>
    `;

    datos.forEach(item => {

        tabla += `
            <tr>
                <td>${item.TransactionID}</td>
                <td>${item.Item}</td>
                <td>${item.Quantity}</td>
                <td>${item.TotalSpent}</td>
            </tr>
        `;

    });

    tabla += `</table>`;

    document.getElementById("resultado").innerHTML = tabla;

}