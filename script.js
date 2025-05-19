// 获取DOM元素
const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const previewArea = document.getElementById('previewArea');
const originalImage = document.getElementById('originalImage');
const compressedImage = document.getElementById('compressedImage');
const originalSize = document.getElementById('originalSize');
const compressedSize = document.getElementById('compressedSize');
const quality = document.getElementById('quality');
const qualityValue = document.getElementById('qualityValue');
const downloadBtn = document.getElementById('downloadBtn');

// 处理文件上传
uploadArea.addEventListener('click', () => fileInput.click());
uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#007AFF';
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.style.borderColor = '#c7c7c7';
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.style.borderColor = '#c7c7c7';
    handleFiles(e.dataTransfer.files);
});

fileInput.addEventListener('change', (e) => handleFiles(e.target.files));

// 处理图片文件
function handleFiles(files) {
    if (!files.length || !files[0].type.startsWith('image/')) return;
    
    const file = files[0];
    const reader = new FileReader();
    
    reader.onload = (e) => {
        originalImage.src = e.target.result;
        originalSize.textContent = formatFileSize(file.size);
        previewArea.hidden = false;
        compressImage();
    };
    
    reader.readAsDataURL(file);
}

// 压缩图片
function compressImage() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    // 等待原始图片加载完成
    originalImage.onload = () => {
        // 设置画布尺寸
        canvas.width = originalImage.naturalWidth;
        canvas.height = originalImage.naturalHeight;
        
        // 绘制图片
        ctx.drawImage(originalImage, 0, 0);
        
        // 压缩图片
        canvas.toBlob((blob) => {
            compressedImage.src = URL.createObjectURL(blob);
            compressedSize.textContent = formatFileSize(blob.size);
            
            // 设置下载按钮
            downloadBtn.onclick = () => {
                const link = document.createElement('a');
                link.href = compressedImage.src;
                link.download = 'compressed-image.jpg';
                link.click();
            };
        }, 'image/jpeg', quality.value / 100);
    };
}

// 质量滑块控制
quality.addEventListener('input', () => {
    qualityValue.textContent = quality.value + '%';
    compressImage();
});

// 格式化文件大小
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
} 