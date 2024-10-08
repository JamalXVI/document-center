db.createUser({
    user: "admin",
    pwd: "admin",
    roles: [
      { role: "readWrite", db: "AcademicDocumentationCenter" },
      { role: "dbAdmin", db: "AcademicDocumentationCenter" }
    ]
  });
  