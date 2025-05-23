/**
 * ملف JavaScript لإدارة المخططات في نظام وكالة السفر والسياحة
 * يعتمد على Chart.js إصدار 3.x
 */

document.addEventListener("DOMContentLoaded", function() {
    // تهيئة المخططات
    initializeCharts();
});

/**
 * تهيئة جميع المخططات
 */
function initializeCharts() {
    // مخطط المبيعات الشهرية (خط بياني)
    if (document.getElementById('salesChart')) {
        initializeSalesChart();
    }
    
    // مخطط توزيع العملاء (دائري)
    if (document.getElementById('pieChart')) {
        initializeCustomerPieChart();
    }
    
    // مخطط التأشيرات (إذا كان موجودًا)
    if (document.getElementById('visasChart')) {
        initializeVisasChart();
    }
}

/**
 * مخطط المبيعات الشهرية (خط بياني)
 */
function initializeSalesChart() {
    const ctx = document.getElementById('salesChart').getContext('2d');
    
    // بيانات المخطط
    const data = {
        labels: ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
        datasets: [{
            label: "الإيرادات (بالريال)",
            backgroundColor: "rgba(78, 115, 223, 0.3)",
            borderColor: "#4e73df",
            pointBackgroundColor: "#4e73df",
            pointBorderColor: "#4e73df",
            pointHoverBackgroundColor: "#4e73df",
            pointHoverBorderColor: "#4e73df",
            data: [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000],
            fill: true
        }]
    };
    
    // خيارات المخطط
    const options = {
        responsive: true,
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 10,
                right: 25,
                top: 25,
                bottom: 0
            }
        },
        scales: {
            x: {
                grid: {
                    display: false,
                    drawBorder: false
                },
                ticks: {
                    font: {
                        family: "Tajawal"
                    },
                    maxTicksLimit: 12
                }
            },
            y: {
                ticks: {
                    font: {
                        family: "Tajawal"
                    },
                    beginAtZero: true,
                    maxTicksLimit: 5,
                    padding: 10
                },
                grid: {
                    color: "rgb(234, 236, 244)",
                    borderColor: "rgb(234, 236, 244)",
                    drawBorder: false,
                    borderDash: [2],
                    borderDashOffset: [2]
                }
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top',
                rtl: true,
                labels: {
                    font: {
                        family: "Tajawal"
                    }
                }
            },
            tooltip: {
                rtl: true,
                titleFont: {
                    family: "Tajawal"
                },
                bodyFont: {
                    family: "Tajawal"
                },
                backgroundColor: "rgb(255,255,255)",
                bodyColor: "#858796",
                titleColor: '#6e707e',
                borderColor: '#dddfeb',
                borderWidth: 1,
                padding: {
                    x: 15,
                    y: 15
                },
                displayColors: false,
                caretPadding: 10
            }
        }
    };
    
    // إنشاء المخطط
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });
}

/**
 * مخطط توزيع العملاء (دائري)
 */
function initializeCustomerPieChart() {
    const ctx = document.getElementById('pieChart').getContext('2d');
    
    // بيانات المخطط
    const data = {
        labels: ["تذاكر طيران", "تأشيرات عمرة", "تأشيرات زيارة", "تأشيرات عمل", "خدمات أخرى"],
        datasets: [{
            backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc", "#f6c23e", "#e74a3b"],
            borderColor: "#ffffff",
            data: [35, 25, 15, 20, 5]
        }]
    };
    
    // خيارات المخطط
    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                position: 'bottom',
                rtl: true,
                labels: {
                    font: {
                        family: "Tajawal"
                    }
                }
            },
            tooltip: {
                rtl: true,
                titleFont: {
                    family: "Tajawal"
                },
                bodyFont: {
                    family: "Tajawal"
                },
                backgroundColor: "rgb(255,255,255)",
                bodyColor: "#858796",
                titleColor: '#6e707e',
                borderColor: '#dddfeb',
                borderWidth: 1,
                padding: {
                    x: 15,
                    y: 15
                }
            }
        }
    };
    
    // إنشاء المخطط
    new Chart(ctx, {
        type: 'pie',
        data: data,
        options: options
    });
}

/**
 * مخطط التأشيرات (خط بياني متعدد)
 */
function initializeVisasChart() {
    const ctx = document.getElementById('visasChart').getContext('2d');
    
    // بيانات المخطط
    const data = {
        labels: ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
        datasets: [
            {
                label: "تأشيرات العمرة",
                backgroundColor: "#4e73df",
                borderColor: "#4e73df",
                data: [45, 50, 38, 41, 35, 28, 32, 35, 50, 65, 75, 80],
                fill: false
            },
            {
                label: "تأشيرات العمل",
                backgroundColor: "#1cc88a",
                borderColor: "#1cc88a",
                data: [20, 25, 30, 35, 40, 45, 40, 35, 30, 25, 20, 15],
                fill: false
            },
            {
                label: "تأشيرات الزيارة",
                backgroundColor: "#f6c23e",
                borderColor: "#f6c23e",
                data: [30, 32, 28, 30, 35, 25, 22, 20, 25, 30, 35, 40],
                fill: false
            }
        ]
    };
    
    // خيارات المخطط
    const options = {
        responsive: true,
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 10,
                right: 25,
                top: 25,
                bottom: 0
            }
        },
        scales: {
            x: {
                grid: {
                    display: false,
                    drawBorder: false
                },
                ticks: {
                    font: {
                        family: "Tajawal"
                    },
                    maxTicksLimit: 12
                }
            },
            y: {
                ticks: {
                    font: {
                        family: "Tajawal"
                    },
                    beginAtZero: true,
                    maxTicksLimit: 5,
                    padding: 10
                },
                grid: {
                    color: "rgb(234, 236, 244)",
                    borderColor: "rgb(234, 236, 244)",
                    drawBorder: false,
                    borderDash: [2],
                    borderDashOffset: [2]
                }
            }
        },
        plugins: {
            legend: {
                display: true,
                position: 'top',
                rtl: true,
                labels: {
                    font: {
                        family: "Tajawal"
                    }
                }
            },
            tooltip: {
                rtl: true,
                titleFont: {
                    family: "Tajawal"
                },
                bodyFont: {
                    family: "Tajawal"
                },
                backgroundColor: "rgb(255,255,255)",
                bodyColor: "#858796",
                titleColor: '#6e707e',
                borderColor: '#dddfeb',
                borderWidth: 1,
                padding: {
                    x: 15,
                    y: 15
                },
                displayColors: false,
                caretPadding: 10
            }
        }
    };
    
    // إنشاء المخطط
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });
}