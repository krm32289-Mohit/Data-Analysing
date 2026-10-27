import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data Load
df = pd.read_csv("Gurgaon_dataset.csv")
print(df)
print(df.columns.tolist())
# print(df.columns)
print(df.info())

#Data Cleaning
df_dup = df.drop_duplicates()
print(df_dup)
df_columns = df.columns.str.strip().str.lower().str.replace(" ","_")
print(df_columns.tolist())

#cleaning the numberic column
df["Price"] = df["Price"].str.replace(",","").astype(int)
print(df['Price'])
df["Rate per sqft"] = df["Rate per sqft"].str.replace(",","").astype(int)
print(df["Rate per sqft"])

#categorical columns cleaning
df['status'] = df['Status'].str.strip().str.lower()
df['RERA_approval'] = df["RERA Approval"].str.strip().str.lower().map({"Approved by RERA":True ,"Not approved by RERA" : False}) 
df["Flat_type"] = df["Flat Type"].str.strip().str.lower()
df = df.drop_duplicates()
print(df)
print(df.info())


print("\nQueston1 :- Which is the costly flat in the dataset?\n")

costly_flat = df.loc[df["Price"].idxmax()]
print(costly_flat)

print("\n//Answer 1//\n")
print(f"The costly flat is a {costly_flat["BHK_Count"]} BHK flat located in {costly_flat["Locality"]} price at {costly_flat["Price"]} crore in {costly_flat["Socity"]} socity.")


print("\nQuestion 2:- which locality has the highest average price?\n")
print("//Answer 2//")
highest_avg_price = df.groupby("Locality")["Price"].mean().idxmax()
print(highest_avg_price)
print("**\n")
print(df.groupby("Locality")["Price"].mean().sort_values(ascending=False).head(10))

print("\nQuestion 3:- Which locality has the highest rate per square foot?\n")
print("//Answer 3//")
high_rate_per_sqft = df.groupby("Locality")["Rate per sqft"].mean().idxmax()
print(f"The locality with the hishest rate per square foot is: {high_rate_per_sqft}.")

print("\nQuestion 4:- Do ready-to-move properties cost more than under-constructions properties")
print("//Answer 4//")
# cost = df.groupby("Status")["Price"].mean().idxmax()
# print(cost)
ready_to_move_avg_price = df[df["Status"]=="Ready to move"]["Price"].mean()
under_construction_avg_price = df[df["Status"]=="Under Construction"]["Price"].mean()
if ready_to_move_avg_price>under_construction_avg_price:
    print("Ready to move properties cost more on average than under-construction properties.")

else:
    print("Under Constructin properties cost more on average than ready to move properties.")
print("\nValues:-Which properties is more than other--\n")
values = df.groupby("Status")["Price"].mean()
print(values)


print("\nQuestion 5:- Do RERA Approved properties command a price premium")
print("//Answer 5//")
rera_approval_avg_price = df[df["RERA Approval"]==True]["Price"].mean()
rera_not_approval_avg_price = df[df["RERA Approval"] == False]["Price"].mean()
if rera_approval_avg_price>rera_not_approval_avg_price:
    print("RERA-Approval properties command a price Premium")

else:
    print("RERA-Approval properties do not command a price Premium")
print("\nValues:-How much RERA Approve the value\n")
value = df.groupby("RERA Approval")["Price"].mean()
print(value)

print("Question 6:- How does area impact price?")
print("\nAnswer 6\n")
# scatter_plt = sns.scatterplot(data=df,x="Area",y="Price")
# print(scatter_plt)
# plt.show()


#by matplotlib

# mat = plt.scatter(df["Area"],df["Price"])
# plt.xlabel("Area")
# plt.ylabel("Price")
# print(mat)
# plt.show()

print("\nQuestion 7:- which BHK configuration is most expensive?")
print("\nAnswer 7")
expensive = df.groupby("BHK_Count")["Price"].mean().idxmax()
print(f"The most expensive BHK configuration on average is {expensive} BHK.")
#value
print(df.groupby("BHK_Count")["Price"].mean().max())
print(df.groupby("BHK_Count")["Price"].mean().idxmax())
print(df.groupby("BHK_Count")["Rate per sqft"].mean().max())
print(df.groupby("BHK_Count")["Rate per sqft"].mean().idxmax())

print("\nQuestion 8:- which property type is the costly?")
print("Answer 8")
costly_property = df.groupby("Flat Type")["Rate per sqft"].mean().idxmax()
print(f"The costly property is {costly_property}.")

print("\nQuestion 9:- Do certain builders price higher?")
print("\nAnswer 9")
print(df.groupby("Company Name")["Rate per sqft"].mean().sort_values(ascending=False).head())
# print(df.groupby("Builder Name")["Rate per sqft"].mean().sort_values(ascending=False).head())


#print name of the top 5
print("**\n")
print(f"The Top 5 builders that price higher are:",end=" ")
top5_builder_name = df.groupby("Company Name")["Rate per sqft"].mean().sort_values(ascending=False).head()
for builder in top5_builder_name:
    print(builder,end=", ")

print("\n")
print("\nQuestion 10:- Are larger homes more expensive per sqft?")
print("\nAnswer 10**")
sns.scatterplot(data=df,x="Area",y="Rate per sqft")
print(f"No,The larger plot are not expensive as per sqft as show in the Graph.")
plt.show()