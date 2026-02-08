import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Quantum 5G Signal Dashboard",
    page_icon="📡",
    layout="wide"
)

# ---------------------------------
# Header
# ---------------------------------
st.markdown("""
# 📡 Quantum-Optimized 5G Signal Dashboard
### Visual comparison of GNU Radio signals before and after Quantum ML optimization
""")

st.divider()

# ---------------------------------
# Load Signals
# ---------------------------------
'''before_signal = np.load("before_signal.npy")
after_signal = np.load("after_signal.npy")

N = 5000  # limit samples for clean visualization
before_signal = before_signal[:N]
after_signal = after_signal[:N]

# ---------------------------------
# KPI Calculations
# ---------------------------------
def avg_power(signal):
    return np.mean(np.abs(signal)**2)

def occupied_bandwidth(signal, threshold=0.1):
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(signal)))
    return np.sum(spectrum > threshold * np.max(spectrum))

# ---------------------------------
# KPI Section
# ---------------------------------
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "Avg Power (Before)",
    f"{avg_power(before_signal):.3f}"
)

kpi2.metric(
    "Avg Power (After)",
    f"{avg_power(after_signal):.3f}"
)

kpi3.metric(
    "Bandwidth Usage (Before)",
    occupied_bandwidth(before_signal)
)

kpi4.metric(
    "Bandwidth Usage (After)",
    occupied_bandwidth(after_signal)
)'''

st.divider()

# ---------------------------------
# Plot Functions
# ---------------------------------
'''def plot_time(signal, title):
    fig, ax = plt.subplots()
    ax.plot(np.abs(signal))
    ax.set_title(title)
    ax.set_xlabel("Sample Index")
    ax.set_ylabel("Amplitude")
    ax.grid(True)
    st.pyplot(fig)

def plot_frequency(signal, title):
    fft = np.fft.fftshift(np.fft.fft(signal))
    freq = np.linspace(-0.5, 0.5, len(fft))

    fig, ax = plt.subplots()
    ax.plot(freq, 20 * np.log10(np.abs(fft) + 1e-6))
    ax.set_title(title)
    ax.set_xlabel("Normalized Frequency")
    ax.set_ylabel("Magnitude (dB)")
    ax.grid(True)
    st.pyplot(fig)'''

# ---------------------------------
# Main Comparison Section
# ---------------------------------
col1, col2 = st.columns(2)

'''with col1:
    st.subheader("🔴 Before Optimization")
    st.caption("Classical / baseline GNU Radio signal")
    plot_time(before_signal, "Time Domain (Before)")
    plot_frequency(before_signal, "Frequency Spectrum (Before)")

with col2:
    st.subheader("🟢 After Quantum Optimization")
    st.caption("Signal after Quantum ML–based optimization")
    plot_time(after_signal, "Time Domain (After)")
    plot_frequency(after_signal, "Frequency Spectrum (After)")'''

st.divider()

# ---------------------------------
# Explanation Section
# ---------------------------------
st.markdown("""
### 📌 What this dashboard shows

- **Time Domain**: Signal stability and amplitude fluctuations  
- **Frequency Domain**: Spectral compactness and leakage  
- **KPIs**: Quantitative comparison of power and bandwidth usage  

The quantum optimizer restructures resource allocation at the PHY/MAC level,
which reflects as **cleaner spectrum usage and improved efficiency**.
""")
