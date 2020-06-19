

DROP TABLE IF EXISTS Websites;

CREATE TYPE ages AS ENUM ('kids', 'teens', 'adults', 'all');
CREATE TYPE categories AS ENUM ('general', 'typing', 'math', 'reading', 'science');

CREATE TABLE Websites (
    website_id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL,
    description text,
    url varchar(100) NOT NULL,
    age ages,
    category categories
);

INSERT INTO Websites ('name', 'description', 'url', 'age', 'category') VALUES
	('Starfall', 'On the Starfall website and in Starfall classrooms, children have fun while learning in an environment of collaboration, wonderment, and play.', 'https://www.starfall.com/h/', 'kids', 'general'),
	('Khan Academy', 'a nonprofit with the mission to provide a free, world-class education for anyone, anywhere.', 'https://www.khanacademy.org/', 'all', 'general'),
    ('edX', 'Founded by Harvard and MIT, edX is home to more than 20 million learners, the majority of top-ranked universities in the world and industry-leading companies. ', 'https://www.edx.org/', 'adults', 'general'),
    ('Coursera', 'Hundreds of free courses give you access to on-demand video lectures, homework exercises, and community discussion forums, taught by top instructors from world-class universities and companies.', 'https://www.coursera.org/', 'adults', 'general')
    ('Docsteach', 'National Archives online resource for teaching with primary documents.', 'https://www.docsteach.org', 'all', 'general'),
    ('Crash Course', 'Tons of awesome courses in one awesome channel!', 'https://www.youtube.com/user/crashcourse/featured', 'all', 'general'),
    ('Digital Public Library of America', 'Empowers people to learn, grow, and contribute to a diverse and better-functioning society by maximizing access to our shared history, culture, and knowledge.', 'https://dp.la', 'all', 'general'),
    ('National Geographic Kids', 'Explore', 'https://kids.nationalgeographic.com/', 'kids', 'science'),
    ('4-H', '4-H welcomes young people from all beliefs and backgrounds, empowering them to create positive change in their communities', 'https://4-h.org/parents/stem-agriculture/', 'kids', 'science'),
    ('Exploratorium', 'The Exploratorium is a public learning laboratory exploring the world through science, art, and human perception.', 'https://www.exploratorium.edu/', 'kids'),
    ('Science Toys', 'Make toys at home with common household materials, often in only a few minutes, that demonstrate fascinating scientific principles.', 'https://scitoys.com/', 'teens', 'science'),
    ('Bill Nye', 'Bill Nye, scientist, engineer, comedian, author, and inventor, is a man with a mission: to help foster a scientifically literate society, to help people everywhere understand and appreciate the science that makes our world work.', 'https://www.billnye.com/the-science-guy', 'kids', 'science'),
    ('Slader', 'Step by step homework solutions. Slader is an independent website supported by millions of students and contributors from all across the globe.', 'teens', 'general'),
    ('Typing', 'https://www.typing.com/', 'all', 'typing'),
    ('Typing Club', '', 'https://www.typingclub.com/kids-typing', 'kids', 'typing'),
    ('Jungle Junior', 'Through the course of about 200 friendly, colorful videos and interactive lessons, kids will learn all about the alphabet and practice sight words, word families, and simple sentences.', 'kids', 'typing'),
    ('Wplfram Alpha', 'Compute expert-level answers using Wolfram’s breakthrough algorithms, knowledge base and AI technology', 'https://www.wolframalpha.com/', 'adults', 'math'),
    ('K-5 Learning', 'Award winning program for after school and summer study. Watch your kids build reading, math and study skills online.', 'https://www.k5learning.com/', 'kids', 'math'),
    ('Purplemath', 'These free lessons are cross-referenced to help you find related material, and the "Search" box on every page is available to help you find whatever math content you''re looking for.', 'https://www.purplemath.com/', 'all', 'math'),
    (''),
    (),
    (),
    ();


