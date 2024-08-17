import streamlit as st
import pandas as pd
import streamlit.components.v1 as components



st.title('Optimizing Supply Chain Logistics: Data Visualization and Cost Minimization Strategies')
st.image('front.jpg')


description, min_cost, about = st.tabs(['Description', 'Cost Minimization', 'About Me'])

with description:
    st.title('About Project')
    st.write("""The primary objective of this analysis is to create a robust framework for optimizing 
             supply chain logistics, considering multiple constraints such as product availability, 
             customer assignments, and freight rates. Using interactive network visualization tools, 
             the project maps out the supply chain network, highlighting key nodes and connections. 
             These visualizations, coupled with a detailed examination of order fulfillment and cost 
             minimization strategies, offer a clear view of the supply chain's operational dynamics. 
             The results not only demonstrate significant cost-saving opportunities but also pave the 
             way for future enhancements and strategic planning in supply chain management.""")
    st.title('Constraints')
    st.write(' **Product Constraints:**')
    st.write("P(i)={p ∈ Products ∣ Pi​ can produce p}")
    st.write(" **Customers Constraints:**")
    st.markdown("C(j)={Pi​ ∈ Plants ∣ Pi​ can serve Cj​}")
    st.write(" **Combined Constraints**")
    st.write("F(o)={Pi∈Plants∣p∈P(i)}∩C(j)")
    
    st.title("Network Analysis")
    HtmlFile = open("plotly_graph.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    components.html(source_code,height=500)
    st.write("""Most facilities have only one connection to a port. Port 4 is potentially the most 
             important one as it has the most connections to the warehouse.""")
    
    st.title('Visualization')
    st.write('**Products Manufactured by Each Plant**')
    st.image('product.jpg')
    
    st.write('**Manufacturing Cost for Each Plant**')
    st.image('plant.jpg')
    
    st.title("Decision Space")
    st.image('decision_space.jpg')
    st.write("""We can see that for most orders, there is only facility that can handle the order. 
             For ~ 1,000 there is no possible facility that can handle the order given our problem
             restrictions, we will exclude these orders from our further optimization problem.""")
    
    st.title("Key Findings")
    st.write("""* **Cost Minimization:** The primary outcome of the project is the identification of the 
             most cost-effective plant and port combinations for order fulfillment. By aggregating and 
             analyzing freight rates, the model effectively minimizes transportation and production costs,
             resulting in significant cost savings.""")
    st.write("""* **Decision-Making Support:** The project provides a data-driven decision-making framework 
             that helps supply chain managers choose the best facilities for order processing. This 
             systematic approach to handling orders ensures that decisions are based on comprehensive 
             analysis rather than intuition or guesswork.""")
    st.write("""* **Constraint Management:** The model incorporates product and customer constraints 
             effectively, ensuring that only feasible plant-port combinations are considered for order 
             fulfillment. This constraint management is crucial for maintaining service levels and meeting 
             contractual obligations with customers. """)
    st.write("""* **Strategic Planning:** The findings support strategic planning by highlighting areas 
             where supply chain operations can be optimized. For instance, the identification of 
             bottlenecks or underutilized facilities provides opportunities for strategic investments and 
             improvements.""")
    st.write("""* **Scalability and Adaptability:** The optimization model is scalable and can adapt to 
             varying levels of demand and changes in the supply chain. This flexibility ensures that the 
             supply chain can respond dynamically to market fluctuations and evolving business needs.""")
    
    st.title("Future Improvements")
    st.write("""* **Incorporate Real-Time Data:** Utilize real-time data from sensors and IoT devices for more 
             accurate and dynamic decision-making.""")
    st.write("""* **Broader Constraint Considerations:** To refine the model, include additional constraints 
             such as labor availability, plant maintenance schedules, and regulatory requirements.""")
    st.write("""* **Multi-Objective Optimization:** Develop a multi-objective optimization model that 
             balances cost minimization with other objectives such as reducing delivery times and 
             improving sustainability.""")
    st.write("""* **Expand Network Analysis:** Extend network analysis to include more granular details 
             such as road conditions, traffic patterns, and transportation mode availability.""")
    st.write("""* **Continuous Improvement Loop:** Implement a continuous improvement loop where the model 
             is regularly updated with new data and insights to keep it relevant and effective.""")
    
with min_cost:
    df = pd.read_csv('decision_cleaned.csv')
    text, port,plant = st.columns(3)
    with text:
        st.write('Choose criteria:')
    with port:
        use_port = st.checkbox('Port')
    with plant:
        use_plant = st.checkbox('Plant')

    if use_plant and use_port:
        plant_list = list(df['plant'].unique())
        plant_list.append(None)
        plant_name = st.selectbox('Select Plant:',plant_list,index=None)
        port_list = list(df['port'].unique())
        port_list.append(None)
        port_name = st.selectbox('Select Port:',port_list,index=None)
        if len(df[(df['port'] == port_name) & (df['plant'] == plant_name)]) != 0:
            cost = int(df[(df['port'] == port_name) & (df['plant'] == plant_name)]['min_cost'].iloc[0])
            port_price = int(df[(df['port'] == port_name) & (df['plant'] == plant_name)]['port_price'].iloc[0])
            orders = len(df[(df['port'] == port_name) & (df['plant'] == plant_name)])
            st.write('**Minimum Cost**:',cost)
            st.write('**Port Name:**',port_name)
            st.write('**Port Price**:',port_price)
            st.write('**Total orders:**',orders)
            st.markdown('---')
        elif plant_name is not None and port_name is not None: 
            st.error("No such data available.")
                
    elif use_port:
        port_list = list(df['port'].unique())
        port_list.append(None)
        port_name = st.selectbox('Select Port:',port_list,index=None)
        plants = list(df[df['port'] == port_name]['plant'].unique())
        for plant in plants:
            cost = df[(df['port'] == port_name) & (df['plant'] == plant)]['min_cost'].iloc[0]
            port_price = df[(df['port'] == port_name) & (df['plant'] == plant)]['port_price'].iloc[0]
            orders = len(df[(df['port'] == port_name) & (df['plant'] == plant)])
            st.write('**Minimum Cost**:',cost)
            st.write('**Port Name:**',port_name)
            st.write('**Port Price**:',port_price)
            st.write('**Total orders:**',orders)
            st.markdown('---')  

    elif use_plant:
        plant_list = list(df['plant'].unique())
        plant_list.append(None)
        plant_name = st.selectbox('Select Plant:',plant_list,index=None)
        ports = list(df[df['plant'] == plant_name]['port'].unique())
        for port in ports:
            cost = df[(df['port'] == port) & (df['plant'] == plant_name)]['min_cost'].iloc[0]
            port_price = df[(df['port'] == port) & (df['plant'] == plant_name)]['port_price'].iloc[0]
            orders = len(df[(df['port'] == port) & (df['plant'] == plant_name)])
            st.write('**Minimum Cost**:',cost)
            st.write('**Port Name:**',port)
            st.write('**Port Price**:',port_price)
            st.write('**Total orders:**',orders)
            st.markdown('---')
with about:
    st.title('**MSc Applied Statistics Student | Aspiring Data Analyst | Passionate about Data-Driven Decision Making**')
    st.write('''
I am a first-year MSc student in Applied Statistics at Symbiosis Statistical Institute, Pune, where I am honing my statistical modeling, data analysis, and predictive analytics skills. My journey into the world of data began with a BSc in Applied Statistics and Analytics from DAVV, Indore, where I developed a deep understanding of statistical theories and their applications in solving complex problems.

With a strong foundation in statistical concepts and a growing proficiency in tools like R, Python, and SQL, I am passionate about driving insights from data to support data-driven decision-making in various industries. My academic projects have involved exploring multivariate statistical techniques, probability theory, and supply chain optimization, all of which have strengthened my analytical and problem-solving abilities.

I am a persistent learner with a curious mind, always eager to explore new methodologies and technologies in the field of data science. I thrive in environments that challenge me to think critically and push the boundaries of my knowledge.

Outside of academics, I find joy in playing cricket and dancing, activities that keep me active and bring balance to my life. These hobbies also foster teamwork, discipline, and creativity, which I bring into my professional life.

I am excited about the opportunities to collaborate with like-minded professionals and organizations that value data-driven insights. Let's connect if you're interested in data analytics, or statistics, or simply want to talk about cricket and dancing!''')            
    #st.markdown("[Linkedin](https://www.linkedin.com/in/kathanshi-jain/)")
    #social=st.container()
    #with social
    Linkedin, Github, Kaggle = st.columns(3)
    Linkedin.markdown("[Linkedin](https://www.linkedin.com/in/kathanshi-jain/)")
    Github.markdown("[Github](https://github.com/Kathanshi0402)")
    Kaggle.markdown("[Kaggle](https://www.kaggle.com/kathanshijain)")