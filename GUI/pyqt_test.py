from pyqt import QMainWindow

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void open(const QUrl &docLocation);

private slots:
    void bookmarkSelected(const QModelIndex &index);

    // action handlers
    void on_actionOpen_triggered();
    void on_actionQuit_triggered();
    void on_actionAbout_triggered();
    void on_actionAbout_Qt_triggered();
    void on_actionZoom_In_triggered();
    void on_actionZoom_Out_triggered();
    void on_actionPrevious_Page_triggered();
    void on_actionNext_Page_triggered();
    void on_actionContinuous_triggered();

private:
    Ui::MainWindow *ui;
The m_zoomSelector variable holds the zoom selector and the m_pageSelector holds the page selector. The m_document variable is an instance of the QPdfDocument class that contains the PDF document.

    ZoomSelector *m_zoomSelector;
    PageSelector *m_pageSelector;

    QPdfDocument *m_document;
};

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
    , m_zoomSelector(new ZoomSelector(this))
    , m_pageSelector(new PageSelector(this))
    , m_document(new QPdfDocument(this))
{

    ui->setupUi(this);

    m_zoomSelector->setMaximumWidth(150);
    ui->mainToolBar->insertWidget(ui->actionZoom_In, m_zoomSelector);

    m_pageSelector->setMaximumWidth(150);
    ui->mainToolBar->addWidget(m_pageSelector);

    m_pageSelector->setPageNavigation(ui->pdfView->pageNavigation());

    connect(m_zoomSelector, &ZoomSelector::zoomModeChanged, ui->pdfView, &QPdfView::setZoomMode);
    connect(m_zoomSelector, &ZoomSelector::zoomFactorChanged, ui->pdfView, &QPdfView::setZoomFactor);
    m_zoomSelector->reset();

    ui->pdfView->setDocument(m_document);

    connect(ui->pdfView, &QPdfView::zoomFactorChanged,
            m_zoomSelector, &ZoomSelector::setZoomFactor);
}