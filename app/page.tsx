import Footer from "@/components/footer";
import Header from "@/components/header";
import { SubHeader } from "@/components/subheader";

export default function Home() {
  return (
    <div className="relative h-[95vh]">
      <Header />
      <SubHeader />
      <Footer />
    </div>
  );
}
