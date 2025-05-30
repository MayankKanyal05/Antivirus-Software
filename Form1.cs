using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AntiVirus
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void miniTimer_Label1_MouseEnter(object sender, EventArgs e)
        {
            miniTimer_Label1.ForeColor = Color.FromArgb(76, 100, 121);
        }

        private void miniTimer_Label1_MouseLeave(object sender, EventArgs e)
        {
            miniTimer_Label1.ForeColor = Color.FromArgb(129, 151, 201);
        }

        private void miniTimer_ThemeContainer1_Click(object sender, EventArgs e)
        {

        }

        private void miniTimer_Label2_MouseEnter(object sender, EventArgs e)
        {
            miniTimer_Label2.ForeColor = Color.FromArgb(76, 100, 121);
        }

        private void miniTimer_Label2_MouseLeave(object sender, EventArgs e)
        {
            miniTimer_Label2.ForeColor = Color.FromArgb(129, 151, 201);
        }

        private void miniTimer_Label3_MouseEnter(object sender, EventArgs e)
        {
            miniTimer_Label3.ForeColor = Color.FromArgb(76, 100, 121);
        }

        private void miniTimer_Label3_MouseLeave(object sender, EventArgs e)
        {
            miniTimer_Label3.ForeColor = Color.FromArgb(129, 151, 201);
        }

        private void panel1_MouseEnter(object sender, EventArgs e)
        {
            //
            panel1.BackColor = Color.FromArgb(200,200, 200);
            playUI_Label1.Text = "Antivirus protects your computer from viruses,spyware,wormd and trojans.\nComputer component is active.";
        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
           
        }

        private void miniTimer_ThemeContainer1_MouseEnter(object sender, EventArgs e)
        {
            panel1.BackColor = Color.FromArgb(238, 238, 238);
            panel3.BackColor = Color.FromArgb(238, 238, 238);
            panel5.BackColor = Color.FromArgb(238, 238, 238);
            playUI_Label1.Text = "";
        }

        private void panel3_MouseEnter(object sender, EventArgs e)
        {
            playUI_Label1.Text = "Web protects you from web-based attacks while you search or surf the internet. It also checks your network\ntraffic for possible threats.";
            panel3.BackColor = Color.FromArgb(200, 200, 200);
        }

        private void panel3_MouseLeave(object sender, EventArgs e)
        {
            
        }

        private void panel5_MouseEnter(object sender, EventArgs e)
        {
            playUI_Label1.Text = "Advanced smartphone protection against viruses, spyware and thieves.";
            panel5.BackColor = Color.FromArgb(200, 200, 200);
        }

        private void panel5_MouseLeave(object sender, EventArgs e)
        {
            
        }
    }
}
