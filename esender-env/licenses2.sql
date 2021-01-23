PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE license_info(
  "license" TEXT,
  "name" TEXT,
  "expiry_date" TEXT,
  "email" TEXT
);
INSERT INTO license_info VALUES('FE1900002','The Grateful Dog Pte Ltd','',NULL);
INSERT INTO license_info VALUES('FE1900006','ISLANDROCK LIMITED LIABILITY PARTNERSHIP','30/6/2021','');
INSERT INTO license_info VALUES('FE1900003','Yappy Pets Pte Ltd','31/5/2021','');
INSERT INTO license_info VALUES('FE2000012','US Dog Bakery Pte Ltd (Vivocity) ','31/8/2021','');
INSERT INTO license_info VALUES('FE1900008','Samtom Trading','30/6/2021','');
INSERT INTO license_info VALUES('FE1900011','Mainland Tropical Fish Farm','31/7/2021','');
INSERT INTO license_info VALUES('FE1900015','Furries Pte Ltd','31/8/2021','');
INSERT INTO license_info VALUES('FE1900009','JUICY MEATS PRIVATE LIMITED','31/7/2021','');
INSERT INTO license_info VALUES('FE2000014','US Dog Bakery Pte Ltd (Nex Mall)','30/9/2021','');
INSERT INTO license_info VALUES('FE1900019','Goodwoofsg LLP','31/8/2021','');
INSERT INTO license_info VALUES('FE1900014','BOM BOM PTE. LTD.','31/8/2021','');
INSERT INTO license_info VALUES('FE1900018','UNDERDOG CO PTE. LTD.','31/8/2021','');
INSERT INTO license_info VALUES('FE1900016','FEED MY PAWS SINGAPORE','31/8/2021','');
INSERT INTO license_info VALUES('FE1900022','Bark Craft Pte Ltd','31/10/2021','');
INSERT INTO license_info VALUES('FE1900021','Semper Fidelis Fine Foods Pte Ltd','30/9/2021','');
INSERT INTO license_info VALUES('FE1900023','Wholesome Paws','31/10/2021','');
INSERT INTO license_info VALUES('FE2000001','Yi Hu Fish Farm Trading','31/12/2020','');
INSERT INTO license_info VALUES('FE1900012','Furry''s Kitchen Pte Ltd','31/7/2021','');
INSERT INTO license_info VALUES('FE2000003','The Barkery Singapore Pte Ltd','31/1/2021','');
INSERT INTO license_info VALUES('FE2000006','Biocomm Pte Ltd','28/2/2021','');
INSERT INTO license_info VALUES('FE1900001','KNIBBLES SINGAPORE','30/4/2021','');
INSERT INTO license_info VALUES('FE1900004','HARVEST & SONS PTE LTD','31/5/2021','');
INSERT INTO license_info VALUES('FE1900025','25 HOLDINGS PTE LTD','30/11/2020','');
INSERT INTO license_info VALUES('FE2000002','MUM MUM GOURMET','31/12/2020','');
INSERT INTO license_info VALUES('FE2000005','TALLAHESSE PTE LTD','28/2/2021','');
INSERT INTO license_info VALUES('FE1900013','INTREPID ASIA VENTURES PRIVATE LIMITED','31/8/2021','');
INSERT INTO license_info VALUES('FE2000009','RAWFOR PAWSG','31/7/2021','');
INSERT INTO license_info VALUES('FE2000010','The Pawsitive Vibes LLP','31/7/2021','');
INSERT INTO license_info VALUES('FE2000013','Pet Axis','31/8/2021','');
INSERT INTO license_info VALUES('FE2000016','PAWFF','31/10/2021','');
INSERT INTO license_info VALUES('FE2222221','example1','15/3/2021','fookloy@cptransform.com');
INSERT INTO license_info VALUES('FE2222222','example2','15/2/2021','fookloy@cptransform.com');
INSERT INTO license_info VALUES('FE2222223','example3','1/2/2021','fookloy@cptransform.com');
INSERT INTO license_info VALUES('',NULL,NULL,NULL);
COMMIT;
