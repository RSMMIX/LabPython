"""
Jean รักษาการผู้บัญชาการของกองอัศวิน Favonius แห่ง Mondstadt ต้องการทราบถึงขุมพลังของอัศวินในแต่ละกลุ่มภายในเมือง Mondstadt แห่งนี้จึงจะทดสอบความแข็งแกร่งของขุมกำลังที่มี โดยจะทำการจัดวางกำลังอัศวินภายในเมือง Mondstadt ดังตัวอย่างต่อไปนี้
                พลัง    :   5  4  4  3  2  2  2
                ลำดับ  :   0  1  2  3  4  5  6
จากข้อมูลข้างต้นประกอบด้วยอัศวินทั้งหมด 7 คน เรียงตามลำดับตั้งแต่ลำดับที่ 0 ถึง 6 และพลังของอัศวินแต่ละคนมีข้อกำหนดดังนี้
    -  อัศวินลำดับที่ n จะมีลูกน้องในสังกัดอยู่ลำดับที่ 2n+1 และ 2n+2 (ลูกน้องของลูกน้องของอัศวินลำดับที่ n ถือว่าเป็นลูกน้องของอัศวินลำดับที่ n ด้วย)
    -  ค่าพลังของอัศวินมีค่าตั้งแต่ 0 - 5
    -  กลุ่มของอัศวินกลุ่มที่ i จะมีสมาชิกคือ อัศวินลำดับที่ i และลูกน้องของอัศวินลำดับที่ i (รวมลูกน้องของลูกน้องของอัศวินด้วย)
    -  พลังของกลุ่มอัศวินลำดับที่ i เป็นพลังรวมของสมาชิกของอัศวินทั้งหมดในกลุ่ม เช่น
            -  อัศวินกลุ่มที่ 1 หมายถึง กลุ่มของอัศวินลำดับที่ 1 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 1, 3 และ 4 และค่าพลังรวมของอัศวินกลุ่มที่ 1 เท่ากับ 4 + 3 + 2 = 9
            -  อัศวินกลุ่มที่ 2 หมายถึง กลุ่มของอัศวินลำดับที่ 2 ซึ่งมีสมาชิกประกอบด้วย อัศวินลำดับที่ 2 , 5 และ 6 และค่าพลังรวมของอัศวินกลุ่มที่ 2 เท่ากับ 4 + 2 + 2 = 8

ดังนั้นเมื่อนำพลังของอัศวินกลุ่มที่ 1 และ 2 มาเทียบกัน จะได้ว่าพลังรวมของอัศวินกลุ่มที่ 1 นั้นมากกว่าพลังรวมของอัศวินกลุ่มที่ 2
Jean ต้องการทราบว่าค่าพลังรวมของอัศวินภายในเมือง Mondstadt เป็นเท่าใด และถ้าเปรียบเทียบระหว่างอัศวินแต่ละกลุ่มแล้วค่าของพลังรวมของอัศวินในกลุ่มใดมีค่ามากกว่ากัน

"""