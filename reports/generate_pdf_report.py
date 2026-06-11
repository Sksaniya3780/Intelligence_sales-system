from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import pandas as pd

from report_templates import (
    report_header,
    report_footer
)


def generate_report(
    data_path,
    output_file="sales_report.pdf"
):

    df = pd.read_csv(data_path)

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            report_header(),
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    total_sales = df["sales_amount"].sum()

    elements.append(
        Paragraph(
            f"Total Sales: ₹ {round(total_sales,2)}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Records: {len(df)}",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            report_footer(),
            styles["Normal"]
        )
    )

    doc.build(elements)

    print(
        f"Report saved as {output_file}"
    )


if __name__ == "__main__":

    generate_report(
        "dataset/processed_sales.csv"
    )