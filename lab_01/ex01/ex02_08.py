def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (Phan tach boi dau phay): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]    

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print(f"Cac so nhi phan chia het cho 5 la: ", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap")