# Worked Beam Example — Lørenskog 3.5 m Kitchen Span

**Part of the formulas-reference skill. Referenced from SKILL.md.**

## 5. KITCHEN BEAM EXAMPLE CALCULATIONS

### 5.1 Load on 3.5m Span, Hip Roof (Lørenskog)

**Assumed data:**
- Roof area width over beam: ~4.5m (perpendicular projection)
- Roof tile + structure: g_k ≈ 0.7 kN/m²
- Attic above: NO live load (structural only)
- Snow zone: 2 (Østlandet)

**Dead load (g_k):**
```
g_k = 0.7 kN/m² × 4.5m wide = 3.15 kN/m  [linear on beam]
```

**Snow load (s_k, characteristic):**
```
s_k = 2.8 kN/m² × 4.5m × cos(35°)  [roof pitch factor]
    ≈ 2.8 × 4.5 × 0.82 ≈ 10.4 kN/m
```

**Design load (ULS, snow governs):**
```
q_d = 1.35 × 3.15 + 1.50 × 10.4
    = 4.25 + 15.6 = 19.85 kN/m  ≈ **20 kN/m**
```

**Max moment:**
```
M_max = (q_d × L²) / 8
      = (20 × 3.5²) / 8
      = (20 × 12.25) / 8
      = 30.6 kNm
```

**Max shear:**
```
V_max = (q_d × L) / 2 = (20 × 3.5) / 2 = 35 kN
```

**Deflection (SLS, live load, quasi-permanent):**
```
q_SLS = g_k + ψ₂ × Q_k
      = 3.15 + 0.6 × 10.4  [ψ₂ for snow ≈ 0.6]
      = 3.15 + 6.24 ≈ 9.4 kN/m

δ_SLS = (5 × q × L⁴) / (384 × E × I)
```

For HEB 180 steel (I ≈ 146,000 cm⁴ = 1.46e8 mm⁴, E = 210,000 MPa):
```
δ_SLS = (5 × 9.4 × 3500⁴) / (384 × 210,000 × 1.46e8)
      ≈ 13 mm  [within L/300 = 11.7 mm limit — marginal]
```

---

