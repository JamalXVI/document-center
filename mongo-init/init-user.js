const bcrypt = require('bcrypt');
const { MongoClient } = require('mongodb');

async function createAdminUser() {
    const uri = "mongodb://admin:password@localhost:27017";
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        await client.connect();
        const db = client.db("AcademicDocumentationCenter");

        const existingAdmin = await db.collection("users").findOne({ username: "admin" });
        if (!existingAdmin) {
            const hashedPassword = await bcrypt.hash("admin", 10);
            await db.collection("users").insertOne({
                username: "admin",
                password_hash: hashedPassword,
                role: "admin"
            });
            console.log("Admin user created successfully.");
        } else {
            console.log("Admin user already exists.");
        }
    } catch (err) {
        console.error("Error creating admin user:", err);
    } finally {
        await client.close();
    }
}

createAdminUser();
