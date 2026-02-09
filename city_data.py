# City Data for Raquel Geo Pages
# Format: slug|name|state|population|top_industries|fun_fact

cities = [
    # ALABAMA (4)
    ("birmingham", "Birmingham", "Alabama", "197,575", "Banking, Healthcare, Steel", "Birthplace of the Civil Rights Movement"),
    ("montgomery", "Montgomery", "Alabama", "196,986", "Government, Manufacturing, Healthcare", "First capital of the Confederacy"),
    ("mobile", "Mobile", "Alabama", "184,952", "Aerospace, Shipping, Tourism", "Home to America's original Mardi Gras"),
    ("huntsville", "Huntsville", "Alabama", "221,933", "Aerospace, Defense, Technology", "Rocket City - where NASA was born"),
    
    # ALASKA (1)
    ("anchorage", "Anchorage", "Alaska", "287,145", "Oil & Gas, Transportation, Tourism", "Larger than Rhode Island in land area"),
    
    # ARIZONA (4) - Phoenix already exists
    ("tucson", "Tucson", "Arizona", "543,242", "Aerospace, Defense, Healthcare", "Home to the University of Arizona and 350+ days of sunshine"),
    ("mesa", "Mesa", "Arizona", "504,258", "Aerospace, Healthcare, Education", "Third-largest city in Arizona"),
    ("chandler", "Chandler", "Arizona", "280,711", "Technology, Manufacturing, Finance", "Intel's largest manufacturing site in the world"),
    ("scottsdale", "Scottsdale", "Arizona", "242,753", "Tourism, Healthcare, Technology", "World-class spa destination and golf capital"),
    
    # ARKANSAS (2)
    ("little-rock", "Little Rock", "Arkansas", "202,591", "Government, Healthcare, Retail", "Home to the Clinton Presidential Library"),
    ("fort-smith", "Fort Smith", "Arkansas", "89,142", "Manufacturing, Healthcare, Retail", "Historic gateway to the Wild West"),
    
    # CALIFORNIA (14) - LA, SD, SJ already exist
    ("san-francisco", "San Francisco", "California", "808,988", "Technology, Finance, Tourism", "Built on 43 hills"),
    ("fresno", "Fresno", "California", "545,567", "Agriculture, Healthcare, Education", "Raisin Capital of the World"),
    ("sacramento", "Sacramento", "California", "525,041", "Government, Healthcare, Education", "Farm-to-Fork Capital of America"),
    ("long-beach", "Long Beach", "California", "451,307", "Shipping, Aerospace, Tourism", "Home to the Queen Mary and 5.5 miles of beaches"),
    ("oakland", "Oakland", "California", "440,646", "Technology, Healthcare, Port Operations", "Birthplace of the Black Panther Party"),
    ("bakersfield", "Bakersfield", "California", "403,455", "Agriculture, Oil & Gas, Logistics", "Country music capital of the West Coast"),
    ("anaheim", "Anaheim", "California", "346,824", "Tourism, Technology, Healthcare", "Home to Disneyland Resort"),
    ("santa-ana", "Santa Ana", "California", "309,441", "Government, Healthcare, Retail", "County seat of Orange County"),
    ("riverside", "Riverside", "California", "314,998", "Education, Healthcare, Manufacturing", "Birthplace of California's citrus industry"),
    ("stockton", "Stockton", "California", "320,804", "Agriculture, Shipping, Healthcare", "California's first city not on the coast"),
    ("chula-vista", "Chula Vista", "California", "275,487", "Tourism, Healthcare, Small Business", "One of the most culturally diverse cities in the US"),
    ("irvine", "Irvine", "California", "309,031", "Technology, Education, Healthcare", "Master-planned community with 54 villages"),
    
    # COLORADO (3)
    ("denver", "Denver", "Colorado", "715,522", "Technology, Aerospace, Healthcare", "The Mile High City - exactly 5,280 feet"),
    ("colorado-springs", "Colorado Springs", "Colorado", "478,961", "Defense, Tourism, Technology", "Home to the US Olympic Training Center"),
    ("aurora", "Aurora", "Colorado", "386,261", "Healthcare, Aerospace, Bioscience", "Colorado's third-largest city"),
    
    # CONNECTICUT (4)
    ("bridgeport", "Bridgeport", "Connecticut", "148,654", "Healthcare, Education, Manufacturing", "Largest city in Connecticut"),
    ("new-haven", "New Haven", "Connecticut", "135,081", "Education, Healthcare, Technology", "Home to Yale University since 1701"),
    ("hartford", "Hartford", "Connecticut", "120,576", "Insurance, Healthcare, Government", "Insurance capital of the world"),
    ("stamford", "Stamford", "Connecticut", "135,470", "Finance, Media, Technology", "Major corporate headquarters hub"),
    
    # DELAWARE (1)
    ("wilmington", "Wilmington", "Delaware", "70,750", "Banking, Legal Services, Healthcare", "Corporate capital with more corporations than people"),
    
    # FLORIDA (11) - Miami already exists
    ("tampa", "Tampa", "Florida", "398,173", "Finance, Healthcare, Tourism", "Home to the world's longest continuous sidewalk"),
    ("orlando", "Orlando", "Florida", "309,154", "Tourism, Technology, Healthcare", "Theme park capital of the world"),
    ("jacksonville", "Jacksonville", "Florida", "950,203", "Finance, Logistics, Healthcare", "Largest city by land area in the continental US"),
    ("st-petersburg", "St. Petersburg", "Florida", "258,308", "Tourism, Healthcare, Financial Services", "Record 768 consecutive days of sunshine"),
    ("hialeah", "Hialeah", "Florida", "222,797", "Retail, Manufacturing, Healthcare", "One of the largest Spanish-speaking communities in the US"),
    ("fort-lauderdale", "Fort Lauderdale", "Florida", "182,760", "Tourism, Marine Industry, Finance", "Yachting capital of the world"),
    ("cape-coral", "Cape Coral", "Florida", "194,016", "Construction, Real Estate, Retail", "More canals than Venice, Italy"),
    ("pembroke-pines", "Pembroke Pines", "Florida", "171,178", "Healthcare, Retail, Education", "One of the best cities to live in America"),
    ("hollywood", "Hollywood", "Florida", "153,067", "Tourism, Healthcare, Retail", "Home to the Hollywood Beach Broadwalk"),
    ("gainesville", "Gainesville", "Florida", "141,085", "Education, Healthcare, Technology", "Home to the University of Florida Gators"),
    ("clearwater", "Clearwater", "Florida", "117,027", "Tourism, Technology, Healthcare", "Home to the Church of Scientology headquarters"),
    
    # GEORGIA (5)
    ("atlanta", "Atlanta", "Georgia", "498,715", "Technology, Film, Finance", "Home to the world's busiest airport"),
    ("augusta", "Augusta", "Georgia", "202,081", "Healthcare, Military, Manufacturing", "Home to the Masters Golf Tournament"),
    ("columbus", "Columbus", "Georgia", "206,922", "Military, Healthcare, Manufacturing", "Home to Fort Benning"),
    ("savannah", "Savannah", "Georgia", "147,780", "Tourism, Shipping, Manufacturing", "America's first planned city"),
    ("athens", "Athens", "Georgia", "127,315", "Education, Healthcare, Music", "Home to the University of Georgia and REM"),
    
    # HAWAII (1)
    ("honolulu", "Honolulu", "Hawaii", "345,510", "Tourism, Defense, Healthcare", "Most remote major city in the world"),
    
    # IDAHO (1)
    ("boise", "Boise", "Idaho", "235,684", "Technology, Healthcare, Manufacturing", "City of Trees in a desert state"),
    
    # ILLINOIS (5) - Chicago already exists
    ("aurora", "Aurora", "Illinois", "180,542", "Manufacturing, Healthcare, Education", "City of Lights - first to use electric lights"),
    ("rockford", "Rockford", "Illinois", "148,655", "Manufacturing, Healthcare, Aerospace", "Former furniture capital of the world"),
    ("joliet", "Joliet", "Illinois", "150,362", "Manufacturing, Healthcare, Logistics", "Home to the oldest public golf course in Illinois"),
    ("naperville", "Naperville", "Illinois", "149,540", "Technology, Healthcare, Retail", "Named best city to live in America multiple times"),
    ("springfield", "Springfield", "Illinois", "114,394", "Government, Healthcare, Education", "State capital and Lincoln's home"),
    
    # INDIANA (4)
    ("indianapolis", "Indianapolis", "Indiana", "887,642", "Manufacturing, Healthcare, Motorsports", "Racing capital of the world"),
    ("fort-wayne", "Fort Wayne", "Indiana", "265,974", "Manufacturing, Healthcare, Defense", "First city with electric street lights"),
    ("evansville", "Evansville", "Indiana", "117,184", "Healthcare, Manufacturing, Education", "Largest city in Southwest Indiana"),
    ("south-bend", "South Bend", "Indiana", "103,395", "Education, Healthcare, Manufacturing", "Home to the University of Notre Dame"),
    
    # IOWA (2)
    ("des-moines", "Des Moines", "Iowa", "212,031", "Insurance, Finance, Healthcare", "Insurance capital with 80+ companies"),
    ("cedar-rapids", "Cedar Rapids", "Iowa", "137,710", "Manufacturing, Food Processing, Healthcare", "Cereal capital of the world"),
    
    # KANSAS (3)
    ("wichita", "Wichita", "Kansas", "395,699", "Aerospace, Manufacturing, Healthcare", "Air capital of the world"),
    ("overland-park", "Overland Park", "Kansas", "197,238", "Technology, Healthcare, Finance", "One of the best places to live in America"),
    ("kansas-city", "Kansas City", "Kansas", "156,607", "Manufacturing, Distribution, Healthcare", "Home to the fastest internet in the US"),
    
    # KENTUCKY (2)
    ("louisville", "Louisville", "Kentucky", "633,045", "Healthcare, Logistics, Manufacturing", "Home to the Kentucky Derby"),
    ("lexington", "Lexington", "Kentucky", "320,347", "Education, Healthcare, Technology", "Horse capital of the world"),
    
    # LOUISIANA (3)
    ("new-orleans", "New Orleans", "Louisiana", "383,997", "Tourism, Energy, Healthcare", "Below sea level but above in spirit"),
    ("baton-rouge", "Baton Rouge", "Louisiana", "227,470", "Petrochemical, Education, Healthcare", "Second largest port in the US by tonnage"),
    ("shreveport", "Shreveport", "Louisiana", "187,593", "Healthcare, Gaming, Manufacturing", "Hollywood South for film production"),
    
    # MAINE (1)
    ("portland", "Portland", "Maine", "68,408", "Tourism, Healthcare, Fishing", "Foodiest small city in America"),
    
    # MARYLAND (2)
    ("baltimore", "Baltimore", "Maryland", "569,931", "Healthcare, Education, Port Operations", "Largest independent city in the US"),
    ("frederick", "Frederick", "Maryland", "85,793", "Biotech, Healthcare, Government", "Clustered Spires skyline"),
    
    # MASSACHUSETTS (4)
    ("boston", "Boston", "Massachusetts", "675,647", "Education, Healthcare, Finance", "America's walking city"),
    ("worcester", "Worcester", "Massachusetts", "206,518", "Healthcare, Education, Manufacturing", "Heart of the Commonwealth"),
    ("springfield", "Springfield", "Massachusetts", "155,929", "Healthcare, Education, Manufacturing", "Birthplace of basketball and Dr. Seuss"),
    ("cambridge", "Cambridge", "Massachusetts", "118,488", "Education, Technology, Biotech", "Home to Harvard and MIT"),
    
    # MICHIGAN (5)
    ("detroit", "Detroit", "Michigan", "632,464", "Automotive, Technology, Healthcare", "Motor City - where cars changed the world"),
    ("grand-rapids", "Grand Rapids", "Michigan", "198,917", "Manufacturing, Healthcare, Technology", "Beer City USA with 80+ breweries"),
    ("warren", "Warren", "Michigan", "139,387", "Automotive, Defense, Healthcare", "GM's Tech Center headquarters"),
    ("sterling-heights", "Sterling Heights", "Michigan", "134,346", "Automotive, Healthcare, Retail", "One of Michigan's safest cities"),
    ("ann-arbor", "Ann Arbor", "Michigan", "123,851", "Education, Technology, Healthcare", "Home to the University of Michigan"),
    
    # MINNESOTA (3)
    ("minneapolis", "Minneapolis", "Minnesota", "429,954", "Finance, Healthcare, Technology", "Birthplace of Prince and Target"),
    ("saint-paul", "Saint Paul", "Minnesota", "311,527", "Government, Education, Healthcare", "State capital - the other Twin City"),
    ("rochester", "Rochester", "Minnesota", "121,465", "Healthcare, Technology, Education", "Home to the Mayo Clinic"),
    
    # MISSISSIPPI (2)
    ("jackson", "Jackson", "Mississippi", "149,761", "Government, Healthcare, Education", "State capital named after Andrew Jackson"),
    ("gulfport", "Gulfport", "Mississippi", "72,926", "Tourism, Shipping, Military", "Second largest city in Mississippi"),
    
    # MISSOURI (4)
    ("kansas-city", "Kansas City", "Missouri", "509,319", "Healthcare, Finance, Manufacturing", "More fountains than Rome"),
    ("st-louis", "St. Louis", "Missouri", "286,578", "Healthcare, Education, Manufacturing", "Gateway to the West"),
    ("springfield", "Springfield", "Missouri", "169,724", "Healthcare, Education, Manufacturing", "Birthplace of Route 66"),
    ("columbia", "Columbia", "Missouri", "126,254", "Education, Healthcare, Insurance", "College town with University of Missouri"),
    
    # MONTANA (1)
    ("billings", "Billings", "Montana", "120,864", "Energy, Healthcare, Agriculture", "Magic City - fastest growing in Montana"),
    
    # NEBRASKA (2)
    ("omaha", "Omaha", "Nebraska", "486,051", "Finance, Healthcare, Agriculture", "Home to Warren Buffett and the College World Series"),
    ("lincoln", "Lincoln", "Nebraska", "292,657", "Education, Government, Healthcare", "State capital and home to University of Nebraska"),
    
    # NEVADA (3)
    ("las-vegas", "Las Vegas", "Nevada", "656,274", "Tourism, Gaming, Conventions", "Entertainment capital of the world"),
    ("henderson", "Henderson", "Nevada", "331,415", "Technology, Healthcare, Tourism", "One of America's safest cities"),
    ("reno", "Reno", "Nevada", "273,448", "Tourism, Technology, Manufacturing", "The biggest little city in the world"),
    
    # NEW HAMPSHIRE (1)
    ("manchester", "Manchester", "New Hampshire", "115,462", "Technology, Healthcare, Education", "Largest city in New Hampshire"),
    
    # NEW JERSEY (5)
    ("newark", "Newark", "New Jersey", "311,549", "Transportation, Healthcare, Education", "Port Newark is largest on the East Coast"),
    ("jersey-city", "Jersey City", "New Jersey", "292,449", "Finance, Technology, Transportation", "Wall Street West"),
    ("paterson", "Paterson", "New Jersey", "159,732", "Manufacturing, Healthcare, Retail", "Silk City - historic textile center"),
    ("elizabeth", "Elizabeth", "New Jersey", "135,772", "Transportation, Manufacturing, Retail", "Home to one of the busiest ports in the US"),
    ("edison", "Edison", "New Jersey", "100,693", "Technology, Healthcare, Retail", "Named after Thomas Edison"),
    
    # NEW MEXICO (2)
    ("albuquerque", "Albuquerque", "New Mexico", "560,504", "Technology, Healthcare, Tourism", "Hot air balloon capital of the world"),
    ("las-cruces", "Las Cruces", "New Mexico", "103,432", "Education, Healthcare, Government", "Home to New Mexico State University"),
    
    # NEW YORK (5) - NYC already exists
    ("buffalo", "Buffalo", "New York", "276,807", "Healthcare, Education, Manufacturing", "Birthplace of the Buffalo wing"),
    ("rochester", "Rochester", "New York", "211,328", "Photography, Healthcare, Education", "Image capital of the world"),
    ("yonkers", "Yonkers", "New York", "211,569", "Healthcare, Education, Retail", "Fourth largest city in New York State"),
    ("syracuse", "Syracuse", "New York", "146,103", "Education, Healthcare, Manufacturing", "Salt City - historic salt production"),
    ("albany", "Albany", "New York", "99,224", "Government, Healthcare, Education", "State capital since 1797"),
    
    # NORTH CAROLINA (5)
    ("charlotte", "Charlotte", "North Carolina", "874,579", "Finance, Healthcare, Energy", "Second largest banking center in the US"),
    ("raleigh", "Raleigh", "North Carolina", "467,665", "Technology, Education, Healthcare", "Part of the Research Triangle"),
    ("greensboro", "Greensboro", "North Carolina", "299,035", "Transportation, Healthcare, Education", "Historic Civil Rights protest site"),
    ("durham", "Durham", "North Carolina", "264,310", "Technology, Healthcare, Education", "Home to Duke University"),
    ("winston-salem", "Winston-Salem", "North Carolina", "249,545", "Healthcare, Manufacturing, Technology", "Camel City - tobacco heritage"),
    
    # NORTH DAKOTA (1)
    ("fargo", "Fargo", "North Dakota", "133,188", "Healthcare, Technology, Education", "Largest city in North Dakota"),
    
    # OHIO (6)
    ("columbus", "Columbus", "Ohio", "905,748", "Education, Healthcare, Retail", "Test market capital of America"),
    ("cleveland", "Cleveland", "Ohio", "372,624", "Healthcare, Manufacturing, Technology", "Rock and Roll Hall of Fame"),
    ("cincinnati", "Cincinnati", "Ohio", "309,317", "Healthcare, Manufacturing, Consumer Goods", "First city founded after the Revolution"),
    ("toledo", "Toledo", "Ohio", "268,508", "Manufacturing, Healthcare, Glass Industry", "Glass capital of the world"),
    ("akron", "Akron", "Ohio", "197,597", "Tires, Healthcare, Polymers", "Rubber capital of the world"),
    ("dayton", "Dayton", "Ohio", "137,571", "Aerospace, Healthcare, Manufacturing", "Birthplace of aviation"),
    
    # OKLAHOMA (3)
    ("oklahoma-city", "Oklahoma City", "Oklahoma", "687,725", "Energy, Aerospace, Healthcare", "Cattle drive history and modern cowboy culture"),
    ("tulsa", "Tulsa", "Oklahoma", "413,066", "Energy, Aerospace, Healthcare", "Oil capital of the world"),
    ("norman", "Norman", "Oklahoma", "128,026", "Education, Research, Healthcare", "Home to the University of Oklahoma"),
    
    # OREGON (3)
    ("portland", "Portland", "Oregon", "652,503", "Technology, Athletic Wear, Healthcare", "Keep it weird - America's weirdest city"),
    ("salem", "Salem", "Oregon", "175,535", "Government, Agriculture, Education", "Cherry city and state capital"),
    ("eugene", "Eugene", "Oregon", "176,654", "Education, Technology, Outdoor Gear", "Track Town USA - birthplace of Nike"),
    
    # PENNSYLVANIA (5)
    ("philadelphia", "Philadelphia", "Pennsylvania", "1,603,797", "Healthcare, Education, Biotechnology", "Birthplace of America"),
    ("pittsburgh", "Pittsburgh", "Pennsylvania", "302,971", "Technology, Healthcare, Education", "City of 446 bridges"),
    ("allentown", "Allentown", "Pennsylvania", "125,845", "Healthcare, Logistics, Manufacturing", "Third largest city in Pennsylvania"),
    ("erie", "Erie", "Pennsylvania", "92,957", "Manufacturing, Healthcare, Tourism", "Great Lakes port city"),
    ("reading", "Reading", "Pennsylvania", "95,112", "Healthcare, Manufacturing, Logistics", "Pagoda city with Japanese architecture"),
    
    # RHODE ISLAND (1)
    ("providence", "Providence", "Rhode Island", "190,934", "Education, Healthcare, Design", "Renaissance city with Ivy League Brown"),
    
    # SOUTH CAROLINA (3)
    ("columbia", "Columbia", "South Carolina", "142,416", "Education, Government, Healthcare", "First city named after Columbus"),
    ("charleston", "Charleston", "South Carolina", "151,612", "Tourism, Healthcare, Technology", "Best city in the world 2016 - Travel+Leisure"),
    ("north-charleston", "North Charleston", "South Carolina", "121,469", "Aerospace, Military, Manufacturing", "Boeing's 787 Dreamliner facility"),
    
    # SOUTH DAKOTA (1)
    ("sioux-falls", "Sioux Falls", "South Dakota", "202,078", "Healthcare, Finance, Retail", "Fastest growing city in the Midwest"),
    
    # TENNESSEE (5)
    ("nashville", "Nashville", "Tennessee", "689,447", "Music, Healthcare, Tourism", "Music City USA - country music capital"),
    ("memphis", "Memphis", "Tennessee", "621,056", "Logistics, Healthcare, Music", "Home of blues, soul, and rock'n'roll"),
    ("knoxville", "Knoxville", "Tennessee", "190,740", "Education, Manufacturing, Healthcare", "Home to the University of Tennessee"),
    ("chattanooga", "Chattanooga", "Tennessee", "186,762", "Manufacturing, Logistics, Tourism", "Gig City - first 10-gig internet"),
    ("clarksville", "Clarksville", "Tennessee", "170,957", "Military, Manufacturing, Healthcare", "Home to Fort Campbell"),
    
    # TEXAS (11) - Houston, San Antonio, Dallas already exist
    ("austin", "Austin", "Texas", "978,908", "Technology, Government, Education", "Live Music Capital of the World"),
    ("fort-worth", "Fort Worth", "Texas", "935,508", "Aviation, Manufacturing, Healthcare", "Where the West begins"),
    ("el-paso", "El Paso", "Texas", "678,415", "Defense, Healthcare, International Trade", "Sun City with 302 days of sun"),
    ("arlington", "Arlington", "Texas", "398,431", "Entertainment, Education, Aerospace", "Home to Six Flags and Cowboys Stadium"),
    ("corpus-christi", "Corpus Christi", "Texas", "317,863", "Energy, Healthcare, Port", "Sparkling City by the Sea"),
    ("plano", "Plano", "Texas", "288,253", "Technology, Finance, Corporate HQ", "Hotbed of corporate relocations"),
    ("laredo", "Laredo", "Texas", "261,639", "International Trade, Logistics, Healthcare", "Largest inland port in the US"),
    ("lubbock", "Lubbock", "Texas", "260,993", "Education, Agriculture, Healthcare", "Hub City of West Texas"),
    ("garland", "Garland", "Texas", "242,037", "Manufacturing, Telecommunications, Healthcare", "City of homes and industries"),
    ("irving", "Irving", "Texas", "254,715", "Technology, Finance, Healthcare", "Las Colinas corporate center"),
    ("amarillo", "Amarillo", "Texas", "200,393", "Energy, Agriculture, Healthcare", "Yellow city and beef capital"),
    
    # UTAH (2)
    ("salt-lake-city", "Salt Lake City", "Utah", "199,723", "Technology, Healthcare, Finance", "Home to the Mormon Tabernacle Choir"),
    ("west-valley-city", "West Valley City", "Utah", "140,230", "Manufacturing, Healthcare, Retail", "Second largest city in Utah"),
    
    # VERMONT (1)
    ("burlington", "Burlington", "Vermont", "44,743", "Education, Healthcare, Tourism", "First city to run entirely on renewable energy"),
    
    # VIRGINIA (5)
    ("virginia-beach", "Virginia Beach", "Virginia", "457,672", "Tourism, Defense, Healthcare", "Longest pleasure beach in the world"),
    ("norfolk", "Norfolk", "Virginia", "230,205", "Defense, Shipping, Healthcare", "Home to the largest naval base in the world"),
    ("chesapeake", "Chesapeake", "Virginia", "249,422", "Defense, Healthcare, Logistics", "One of the fastest growing cities in Virginia"),
    ("richmond", "Richmond", "Virginia", "226,604", "Government, Finance, Healthcare", "Former capital of the Confederacy"),
    ("newport-news", "Newport News", "Virginia", "184,587", "Shipbuilding, Defense, Healthcare", "Shipbuilding capital of the US"),
    
    # WASHINGTON (4)
    ("seattle", "Seattle", "Washington", "749,256", "Technology, Aerospace, Healthcare", "Birthplace of Starbucks and Amazon"),
    ("spokane", "Spokane", "Washington", "228,989", "Healthcare, Education, Manufacturing", "Largest city between Seattle and Minneapolis"),
    ("tacoma", "Tacoma", "Washington", "219,346", "Healthcare, Manufacturing, Port", "City of Destiny on Puget Sound"),
    ("vancouver", "Vancouver", "Washington", "194,512", "Technology, Manufacturing, Healthcare", "Gateway to the Pacific Northwest"),
    
    # WEST VIRGINIA (1)
    ("charleston", "Charleston", "West Virginia", "48,864", "Government, Healthcare, Chemicals", "State capital with chemical heritage"),
    
    # WISCONSIN (3)
    ("milwaukee", "Milwaukee", "Wisconsin", "577,222", "Manufacturing, Healthcare, Brewing", "Beer capital of the world"),
    ("madison", "Madison", "Wisconsin", "280,305", "Education, Government, Technology", "Most educated city in America"),
    ("green-bay", "Green Bay", "Wisconsin", "107,395", "Manufacturing, Healthcare, Paper", "Titletown USA - Packers champions"),
    
    # WYOMING (1)
    ("cheyenne", "Cheyenne", "Wyoming", "65,132", "Government, Military, Transportation", "State capital and rodeo capital"),
    
    # DISTRICT OF COLUMBIA (1)
    ("washington-dc", "Washington DC", "District of Columbia", "712,816", "Government, Consulting, Technology", "Federal capital since 1790"),
]

# Verify count
print(f"Total cities to generate: {len(cities)}")
