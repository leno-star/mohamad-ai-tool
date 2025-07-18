document.getElementById("generateBtn").addEventListener("click", async () => {
  const product = document.getElementById("productName").value;
  const pattern = document.getElementById("scriptType").value;

  if (!product || !pattern) {
    alert("يرجى إدخال اسم المنتج واختيار النمط");
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/generate-script", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ product, pattern })
    });

    const data = await response.json();

    if (data.script) {
      document.getElementById("scriptOutput").textContent = data.script;
    } else {
      document.getElementById("scriptOutput").textContent = "حدث خطأ أثناء التوليد.";
    }
  } catch (error) {
    console.error("خطأ:", error);
    document.getElementById("scriptOutput").textContent = "تعذر الاتصال بالخادم.";
  }
});