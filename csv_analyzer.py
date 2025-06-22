import csv
import sqlite3
from datetime import datetime, timedelta
import random
import statistics

class CSVAnalyzer:
    """Professional CSV Data Analysis Tool"""
    
    def __init__(self):
        self.data = []
        self.headers = []
        self.filename = None
        self.numerical_columns = []
        self.categorical_columns = []
    
    def generate_sample_data(self, filename="sample_data.csv", records=1000):
        """Generate realistic sample CSV data for testing"""
        print(f"Generating {records} sample records...")
        
        # Sample data
        products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Mouse']
        regions = ['North', 'South', 'East', 'West']
        categories = ['Electronics', 'Accessories']
        
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Headers
            headers = ['Date', 'Product', 'Category', 'Price', 'Quantity', 'Region', 'Total_Sales']
            writer.writerow(headers)
            
            # Generate data
            for i in range(records):
                date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
                product = random.choice(products)
                category = random.choice(categories)
                price = round(random.uniform(50, 1000), 2)
                quantity = random.randint(1, 5)
                region = random.choice(regions)
                total_sales = round(price * quantity, 2)
                
                writer.writerow([date, product, category, price, quantity, region, total_sales])
        
        print(f"✓ Created {filename} with {records} records")
        return filename
    
    def load_csv(self, filename):
        """Load CSV file with error handling"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.headers = next(reader)
                self.data = list(reader)
            
            self.filename = filename
            self._detect_column_types()
            print(f"✓ Loaded {filename}: {len(self.data)} rows, {len(self.headers)} columns")
            return True
            
        except FileNotFoundError:
            print(f"✗ File not found: {filename}")
            return False
        except Exception as e:
            print(f"✗ Error loading file: {e}")
            return False
    
    def _detect_column_types(self):
        """Automatically detect numerical vs categorical columns"""
        self.numerical_columns = []
        self.categorical_columns = []
        
        for col_idx, header in enumerate(self.headers):
            # Sample first 100 values
            sample_values = []
            for row in self.data[:100]:
                if col_idx < len(row) and row[col_idx].strip():
                    sample_values.append(row[col_idx].strip())
            
            if not sample_values:
                continue
            
            # Count how many values are numeric
            numeric_count = 0
            for value in sample_values:
                try:
                    float(value.replace(',', ''))
                    numeric_count += 1
                except ValueError:
                    pass
            
            # If 80%+ are numeric, classify as numerical
            if numeric_count / len(sample_values) > 0.8:
                self.numerical_columns.append(header)
            else:
                self.categorical_columns.append(header)
    
    def show_overview(self):
        """Display clean dataset overview"""
        if not self.data:
            print("No data loaded")
            return
        
        print("\n" + "="*60)
        print("DATASET OVERVIEW")
        print("="*60)
        print(f"File: {self.filename}")
        print(f"Size: {len(self.data):,} rows × {len(self.headers)} columns")
        
        print(f"\nColumns:")
        for i, header in enumerate(self.headers, 1):
            col_type = "Numerical" if header in self.numerical_columns else "Categorical"
            print(f"  {i:2d}. {header:20} ({col_type})")
        
        print(f"\nSample data:")
        for i, row in enumerate(self.data[:3], 1):
            print(f"  Row {i}: {row}")
    
    def analyze_numerical(self, column_name):
        """Analyze numerical column with clean output"""
        if column_name not in self.numerical_columns:
            print(f"'{column_name}' is not a numerical column")
            return
        
        col_idx = self.headers.index(column_name)
        values = []
        
        # Extract numerical values
        for row in self.data:
            if col_idx < len(row) and row[col_idx].strip():
                try:
                    values.append(float(row[col_idx].replace(',', '')))
                except ValueError:
                    continue
        
        if not values:
            print(f"No valid data in {column_name}")
            return
        
        # Calculate statistics
        print(f"\n{column_name.upper()} - ANALYSIS")
        print("-" * 40)
        print(f"Count:      {len(values):,}")
        print(f"Mean:       {statistics.mean(values):,.2f}")
        print(f"Median:     {statistics.median(values):,.2f}")
        print(f"Min:        {min(values):,.2f}")
        print(f"Max:        {max(values):,.2f}")
        print(f"Range:      {max(values) - min(values):,.2f}")
        
        if len(values) > 1:
            print(f"Std Dev:    {statistics.stdev(values):,.2f}")
    
    def analyze_categorical(self, column_name, top=10):
        """Analyze categorical column with clean output"""
        if column_name not in self.categorical_columns:
            print(f"'{column_name}' is not a categorical column")
            return
        
        col_idx = self.headers.index(column_name)
        counts = {}
        
        # Count values
        for row in self.data:
            if col_idx < len(row) and row[col_idx].strip():
                value = row[col_idx].strip()
                counts[value] = counts.get(value, 0) + 1
        
        if not counts:
            print(f"No data in {column_name}")
            return
        
        # Sort by frequency
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\n{column_name.upper()} - ANALYSIS")
        print("-" * 40)
        print(f"Unique values: {len(counts)}")
        print(f"Total records: {sum(counts.values())}")
        
        print(f"\nTop {min(top, len(sorted_counts))} values:")
        for value, count in sorted_counts[:top]:
            percentage = count / sum(counts.values()) * 100
            print(f"  {value:15} {count:6,} ({percentage:5.1f}%)")
    
    def export_to_database(self, db_name="data_analysis.db"):
        """Export data to SQLite database"""
        if not self.data:
            print("No data to export")
            return False
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Create table
        table_name = "csv_data"
        columns = []
        for header in self.headers:
            clean_name = header.replace(' ', '_').replace('-', '_').lower()
            col_type = "REAL" if header in self.numerical_columns else "TEXT"
            columns.append(f"{clean_name} {col_type}")
        
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"""
            CREATE TABLE {table_name} (
                id INTEGER PRIMARY KEY,
                {', '.join(columns)}
            )
        """)
        
        # Insert data
        placeholders = ', '.join(['?' for _ in self.headers])
        cursor.executemany(f"INSERT INTO {table_name} ({', '.join([h.replace(' ', '_').replace('-', '_').lower() for h in self.headers])}) VALUES ({placeholders})", self.data)
        
        conn.commit()
        conn.close()
        
        print(f"✓ Exported {len(self.data)} rows to {db_name}")
        return True
    
    def generate_report(self):
        """Generate clean analysis report"""
        if not self.data:
            print("No data loaded")
            return
        
        print("\n" + "="*60)
        print("DATA ANALYSIS REPORT")
        print("="*60)
        print(f"Dataset: {self.filename}")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Quick stats
        print(f"\nQuick Statistics:")
        print(f"  Total rows: {len(self.data):,}")
        print(f"  Total columns: {len(self.headers)}")
        print(f"  Numerical columns: {len(self.numerical_columns)}")
        print(f"  Categorical columns: {len(self.categorical_columns)}")
        
        # Analyze key columns
        if self.numerical_columns:
            print(f"\nNumerical Analysis:")
            for col in self.numerical_columns[:3]:  # First 3 numerical columns
                self.analyze_numerical(col)
        
        if self.categorical_columns:
            print(f"\nCategorical Analysis:")
            for col in self.categorical_columns[:3]:  # First 3 categorical columns
                self.analyze_categorical(col, top=5)

def main():
    """Main function with clean interface"""
    analyzer = CSVAnalyzer()
    
    print("CSV DATA ANALYZER")
    print("=" * 50)
    
    # Generate sample data
    sample_file = analyzer.generate_sample_data("sales_data.csv", 500)
    
    # Load and analyze
    if analyzer.load_csv(sample_file):
        # Show overview
        analyzer.show_overview()
        
        # Generate comprehensive report
        analyzer.generate_report()
        
        # Export to database
        analyzer.export_to_database()

if __name__ == "__main__":
    main()