package tpn5;

public class Coureur implements ILoisir {
	
	public void CourirOuMarcher() {
		System.out.println("je cours "+distance+" km");
	}
	
	public void CourirMoins() {
		System.out.println("je cours " +  distance/2 + " km");
	}
	

}
