using System;
using System.Windows.Forms;
using System.Drawing;


namespace alex{
	class Alex{
		public int prt;
		public int nprt;
		public int oth = 1;
		protected Random rnd;

		public Alex(){
			this.rnd = new Random();
			this.prt = rnd.Next(1, 4);
			if(this.prt == 1)
				this.oth ++;
			this.nprt = rnd.Next(1,3);
			if(this.prt == 1 || this.prt == this.nprt)
				nprt ++;
			if(this.oth == this.nprt){
				if(this.oth != 1)
					this.oth ++;
				else{
					if(this.prt == 2)
						this.oth = 3;
					else
						this.oth = 2;
				}
			}
		}
	}


	class Gui : Form{
		Button[] bts;
		Alex ct;
		bool prima;
		Label lbl;
		Label ll;
		bool stop;
		Button bb;
		Label lb;
		PictureBox alx;
		PictureBox[] prts;

		public Gui(){
			this.prts = new PictureBox[3];
			for(int i=0;i<3;i++){
				this.prts[i] = new PictureBox();
				this.prts[i].Image = Image.FromFile("prt.png");
			}
			this.Size = new Size(400, 400);
			this.lbl = new Label();
			this.ll = new Label();
			bts = new Button[3];
			this.ct = new Alex();
			this.bb = new Button();
			this.bb.Text = "Jogar Novamente";
			this.bb.Click += this.jogarNovamente;
			this.bb.Size = new Size(150, 25);
			this.alx = new PictureBox();
			this.alx.Image = Image.FromFile("Alex.png");

		}

		public void jogarNovamente(object sender, EventArgs e){
			Button me = sender as Button;
			this.Controls.Remove(me);
			this.Controls.Remove(this.lbl);
			this.ct = new Alex();
			this.prima = true;
			this.stop = false;
			foreach(Button b in this.bts){
				this.Controls.Remove(b);
			}
			foreach(PictureBox pb in this.prts){
				this.Controls.Remove(pb);
			}
			this.Controls.Remove(this.lb);
			this.Controls.Remove(alx);
			this.Run();
		}

		public void Clicker(object sender, EventArgs e){
			Button me = sender as Button;
			this.ll.Text = "Faca a decisao final";
			this.ll.Size = new Size(120, 30);
			this.ll.Location = new Point(this.Width / 10, this.Height * 3 / 5 + 15);
			this.lbl.Size = new Size(200, 15);
			this.lbl.Location = new Point(this.Width / 10, this.Height * 3  / 5);
			
			int ch = Convert.ToInt32(me.Text[me.Text.Length - 1]) - 48;
			if(this.prima){
				if(ch != this.ct.nprt){
					this.Controls.Remove(this.bts[this.ct.nprt - 1]);
					this.lbl.Text = "Alex nao esta na porta " + this.ct.nprt;
					this.Controls.Remove(this.prts[this.ct.nprt - 1]);
				}else{
					this.Controls.Remove(this.bts[this.ct.oth - 1]);
					this.lbl.Text = "Alex nao esta na porta " + this.ct.oth ;
					this.Controls.Remove(this.prts[this.ct.oth - 1]);
				}
				this.Controls.Add(this.lbl);
				this.Controls.Add(this.ll);
				this.prima = false;
			}else if(this.stop == false){
				this.Controls.Remove(this.lbl);
				this.Controls.Remove(this.ll);
				if(ch == ct.prt){
					this.lbl.Text = "Voce encontrou Alex";
				}else{
					this.lbl.Text = "Voce perdeu";
				}
				this.stop = true;
				this.Controls.Add(this.lbl);
				this.bb.Location = new Point(4 * this.Width / 5 - 100, 4 * this.Height / 5);
				this.Controls.Add(this.bb);
				foreach(PictureBox pb in this.prts){
					this.Controls.Remove(pb);
				}
			}
			

		}

		public void Run(){
			this.lb = new Label();
			this.lb.Text = "Encontre Alex";
			this.lb.Location = new Point(this.Width / 2, 10);
			this.prima = true;
			this.stop = false;
			this.alx.Location = new Point(this.ct.prt * this.Width / 4, this.Height / 3);
			for(int i =0;i<3;i++){
				this.bts[i] = new Button();
				this.bts[i].Text = "Porta " + (i+1);
			       	this.bts[i].Location = new Point((i +1) * this.Width / 4, this.Height / 2);	
				this.bts[i].Click += this.Clicker;
				this.prts[i].Location = new Point((i +1) * this.Width / 4, this.Height / 3);
				this.Controls.Add(this.bts[i]);
				this.Controls.Add(this.prts[i]);
			}
			this.Controls.Add(lb);
			this.Controls.Add(alx);
			Application.Run(this);
		}
	}

	class Prog{
		static void Main(string[] args){
			Gui g = new Gui();
			g.Run();
		}
	}

}
