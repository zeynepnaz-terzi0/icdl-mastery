import sys, re, shutil
sys.stdout.reconfigure(encoding='utf-8')

path = "C:/Users/Windows 10/Desktop/r ta/icdl_study_app.html"
with open(path, encoding='utf-8') as f:
    content = f.read()

# Each lecture is inserted right before the module's `flashcards:` key.
# We find the unique flashcards marker for each module and insert lecture before it.

lectures = {}

# ── MODULE 0 – Computer Essentials ───────────────────────────────────────────
lectures[0] = r"""    lecture: [
      {
        title: "L1 · The Computer: History & Types",
        body: `
          <h4>A Brief History</h4>
          <p>The first electronic computers appeared in the 1940s and filled entire rooms. ENIAC (1945) used 18,000 vacuum tubes and consumed 150 kilowatts of power. By the 1970s, the microprocessor allowed computers to shrink to desktop size. Today a smartphone contains more processing power than the entire Apollo mission computer system.</p>
          <h4>Types of Computers</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Type</th><th style="padding:8px;text-align:left">Description</th><th style="padding:8px;text-align:left">Example users</th></tr>
            <tr><td style="padding:8px"><strong>Mainframe</strong></td><td style="padding:8px">Massive, expensive, handles millions of transactions simultaneously</td><td style="padding:8px">Banks, airlines, governments</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Server</strong></td><td style="padding:8px">Provides services to other computers; runs 24/7</td><td style="padding:8px">Web hosting, email, file sharing</td></tr>
            <tr><td style="padding:8px"><strong>Desktop</strong></td><td style="padding:8px">Non-portable, separate components (tower + monitor)</td><td style="padding:8px">Office workers, gamers</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Laptop</strong></td><td style="padding:8px">Portable, built-in screen, keyboard, battery</td><td style="padding:8px">Students, travelers</td></tr>
            <tr><td style="padding:8px"><strong>Tablet</strong></td><td style="padding:8px">Touch-screen, no physical keyboard, very portable</td><td style="padding:8px">Casual browsing, reading</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Smartphone</strong></td><td style="padding:8px">Pocket-sized, phone + computer + camera</td><td style="padding:8px">General consumers</td></tr>
          </table>
        `
      },
      {
        title: "L2 · Inside the Computer: Hardware in Depth",
        body: `
          <h4>The CPU (Central Processing Unit)</h4>
          <p>The CPU is the brain of the computer. It performs the <strong>fetch-decode-execute cycle</strong> billions of times per second:</p>
          <ol>
            <li><strong>Fetch</strong> — retrieves the next instruction from RAM</li>
            <li><strong>Decode</strong> — the Control Unit interprets the instruction</li>
            <li><strong>Execute</strong> — the ALU carries out the instruction</li>
          </ol>
          <p><strong>CPU Components:</strong></p>
          <ul>
            <li><strong>ALU</strong> (Arithmetic and Logic Unit) — performs maths (+, -, ×, ÷) and logical comparisons (>, <, =)</li>
            <li><strong>Control Unit (CU)</strong> — coordinates all CPU operations and the flow of data</li>
            <li><strong>Cache</strong> — ultra-fast memory inside the CPU (L1, L2, L3 cache). Stores frequently used data so the CPU doesn't have to fetch it from slower RAM</li>
            <li><strong>Registers</strong> — tiny, extremely fast storage holding the current instruction and data being processed</li>
            <li><strong>Clock Speed</strong> — measured in GHz (gigahertz). A 3.5 GHz CPU processes 3.5 billion cycles per second</li>
          </ul>
          <h4>Memory: RAM vs ROM</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Feature</th><th style="padding:8px;text-align:left">RAM</th><th style="padding:8px;text-align:left">ROM</th></tr>
            <tr><td style="padding:8px">Full name</td><td style="padding:8px">Random Access Memory</td><td style="padding:8px">Read-Only Memory</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Volatile?</td><td style="padding:8px">Yes — data lost when power off</td><td style="padding:8px">No — data permanent</td></tr>
            <tr><td style="padding:8px">Purpose</td><td style="padding:8px">Working memory — holds running programs and open files</td><td style="padding:8px">Stores BIOS — startup instructions</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Speed</td><td style="padding:8px">Very fast</td><td style="padding:8px">Slower</td></tr>
            <tr><td style="padding:8px">Modifiable?</td><td style="padding:8px">Yes — constantly changing</td><td style="padding:8px">No (or very limited)</td></tr>
          </table>
          <h4>Storage Devices</h4>
          <ul>
            <li><strong>HDD (Hard Disk Drive)</strong> — magnetic spinning platters; cheap storage, slower, fragile (moving parts)</li>
            <li><strong>SSD (Solid State Drive)</strong> — flash memory; faster, more durable, more expensive per GB than HDD</li>
            <li><strong>USB Flash Drive</strong> — portable flash storage; plug-and-play</li>
            <li><strong>Optical Disc (CD/DVD/Blu-ray)</strong> — laser reads/writes data; used for distributing software and media</li>
          </ul>
          <h4>Data Units — From Bit to Terabyte</h4>
          <p>All data is ultimately stored as bits (0 or 1). Units scale up in powers of 1024:</p>
          <p style="font-family:monospace;background:var(--bg-card2);padding:10px;border-radius:6px">
            1 bit → 8 bits = 1 Byte → 1024 B = 1 KB → 1024 KB = 1 MB → 1024 MB = 1 GB → 1024 GB = 1 TB
          </p>
        `
      },
      {
        title: "L3 · Input, Output & Peripheral Devices",
        body: `
          <h4>Input Devices</h4>
          <p>Input devices send data <strong>into</strong> the computer:</p>
          <ul>
            <li><strong>Keyboard</strong> — most common input device; QWERTY layout is standard</li>
            <li><strong>Mouse</strong> — pointing device; controls cursor position. Variations: trackpad, trackball</li>
            <li><strong>Scanner</strong> — converts physical documents/photos into digital images</li>
            <li><strong>Microphone</strong> — captures sound for recording or voice recognition</li>
            <li><strong>Webcam</strong> — captures video for video calling, recording</li>
            <li><strong>Barcode reader</strong> — scans product barcodes (used in supermarkets)</li>
            <li><strong>Touchscreen</strong> — both INPUT (touch) and OUTPUT (display) — dual-purpose</li>
            <li><strong>Digital camera</strong> — captures still images and video digitally</li>
          </ul>
          <h4>Output Devices</h4>
          <p>Output devices send data <strong>out of</strong> the computer to the user:</p>
          <ul>
            <li><strong>Monitor</strong> — visual display unit (VDU); displays text, images, video. Resolution measured in pixels (e.g., 1920×1080 Full HD)</li>
            <li><strong>Printer</strong> — produces physical (hard copy) output
              <ul>
                <li><em>Inkjet</em> — sprays ink; good for photos, quiet, slower</li>
                <li><em>Laser</em> — uses heat and toner powder; fast, high volume, best for text</li>
              </ul>
            </li>
            <li><strong>Speakers / Headphones</strong> — audio output</li>
            <li><strong>Plotter</strong> — draws precise vector graphics; used in architecture and engineering</li>
            <li><strong>Projector</strong> — displays screen content on a large surface for presentations</li>
          </ul>
        `
      },
      {
        title: "L4 · Software: Operating Systems & Applications",
        body: `
          <h4>What is Software?</h4>
          <p>Software is a set of instructions that tells hardware what to do. Without software, hardware is a useless collection of components. There are two fundamental categories:</p>
          <h4>1. System Software</h4>
          <p><strong>Operating System (OS)</strong> — the master program that manages all hardware and provides a platform for other software. Responsibilities:</p>
          <ul>
            <li>Manages CPU time between running processes (multitasking)</li>
            <li>Manages memory (RAM allocation)</li>
            <li>Controls input/output devices via device drivers</li>
            <li>Provides a user interface (GUI or command line)</li>
            <li>Manages the file system (creating, reading, writing, deleting files)</li>
            <li>Enforces security (user accounts, permissions)</li>
          </ul>
          <p>Examples: Windows 11, macOS Ventura, Ubuntu Linux, Android, iOS</p>
          <h4>2. Application Software</h4>
          <p>Programs that perform specific tasks for the user:</p>
          <ul>
            <li>Word processors (Writer, Word)</li>
            <li>Spreadsheets (Calc, Excel)</li>
            <li>Web browsers (Firefox, Chrome)</li>
            <li>Email clients (Thunderbird, Outlook)</li>
            <li>Graphic editors (GIMP, Photoshop)</li>
          </ul>
          <h4>Software Licensing Types</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Licence</th><th style="padding:8px;text-align:left">What it means</th><th style="padding:8px;text-align:left">Example</th></tr>
            <tr><td style="padding:8px"><strong>Commercial/Proprietary</strong></td><td style="padding:8px">Purchase required; source code hidden; cannot modify</td><td style="padding:8px">Microsoft Office</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Shareware</strong></td><td style="padding:8px">Try before you buy (limited time/features)</td><td style="padding:8px">WinZip trial</td></tr>
            <tr><td style="padding:8px"><strong>Freeware</strong></td><td style="padding:8px">Free to use, cannot modify; author keeps copyright</td><td style="padding:8px">Skype</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Open Source</strong></td><td style="padding:8px">Source code public; can modify and redistribute</td><td style="padding:8px">Linux, Firefox, LibreOffice</td></tr>
            <tr><td style="padding:8px"><strong>Public Domain</strong></td><td style="padding:8px">No copyright; completely free to use, copy, modify</td><td style="padding:8px">Some old software</td></tr>
          </table>
          <p><strong>EULA</strong> (End User Licence Agreement) — the legal contract between the software publisher and user. You agree to this when installing software. Key restrictions: no copying, no reverse engineering, limited number of installs.</p>
        `
      },
      {
        title: "L5 · Networks: LAN, WAN, Internet & WWW",
        body: `
          <h4>Why Network Computers?</h4>
          <p>A computer network connects devices so they can share resources (files, printers, internet) and communicate. Without networks, every computer would be isolated and data sharing would require physical media (USB drives, CDs).</p>
          <h4>Network Types</h4>
          <ul>
            <li><strong>LAN (Local Area Network)</strong> — covers a small area (one building, campus). Typically connected by Ethernet cable or Wi-Fi. Fast (100 Mbps to 10 Gbps). Owned and managed by the organisation.</li>
            <li><strong>WAN (Wide Area Network)</strong> — covers a large geographic area (cities, countries). Uses leased telephone lines, fibre, or satellite. The <strong>Internet</strong> is the world's largest WAN.</li>
            <li><strong>WLAN (Wireless LAN)</strong> — a LAN using Wi-Fi (IEEE 802.11 standard) instead of cables. Convenient but potentially less secure than wired.</li>
          </ul>
          <h4>Internet vs World Wide Web</h4>
          <p>These are often confused but are fundamentally different:</p>
          <ul>
            <li><strong>Internet</strong> = the global physical network infrastructure (cables, routers, servers). It supports many services: WWW, email, FTP, VoIP.</li>
            <li><strong>World Wide Web (WWW)</strong> = a collection of web pages (HTML documents) stored on web servers, linked by hyperlinks, accessed via a browser. It is ONE SERVICE that runs on the Internet.</li>
          </ul>
          <h4>Connection Types</h4>
          <ul>
            <li><strong>ADSL</strong> (Asymmetric DSL) — broadband over phone lines. 'Asymmetric' = download faster than upload. Suitable for home users.</li>
            <li><strong>Fibre optic</strong> — uses light through glass fibre; much faster than ADSL (up to 1 Gbps+)</li>
            <li><strong>Cable</strong> — uses TV cable infrastructure; shared bandwidth in a neighbourhood</li>
            <li><strong>Mobile (4G/5G)</strong> — wireless broadband via cellular networks</li>
            <li><strong>Satellite</strong> — useful in remote areas; high latency (delay)</li>
          </ul>
          <p>You connect to the Internet through an <strong>ISP (Internet Service Provider)</strong> such as BT, Virgin, Vodafone, or Turkcell.</p>
        `
      },
      {
        title: "L6 · Health, Safety, Law & Ethics",
        body: `
          <h4>Health Risks of Computer Use</h4>
          <ul>
            <li><strong>RSI (Repetitive Strain Injury)</strong> — damage to muscles, tendons, nerves from repetitive movements (typing, mouse use). Affects wrists, hands, arms. Prevention: take breaks, use ergonomic equipment.</li>
            <li><strong>Eye strain (Computer Vision Syndrome)</strong> — caused by prolonged screen use. Symptoms: headaches, blurred vision, dry eyes. Prevention: 20-20-20 rule (every 20 min, look 20 feet away for 20 seconds); reduce screen glare.</li>
            <li><strong>Back/neck pain</strong> — poor posture at workstations. Prevention: ergonomic chair, monitor at eye level, feet flat on floor.</li>
            <li><strong>Stress and fatigue</strong> — information overload, constant connectivity. Prevention: regular breaks, healthy work-life balance.</li>
          </ul>
          <h4>Ergonomic Workstation Setup</h4>
          <ul>
            <li>Monitor: arm's length away, top of screen at eye level</li>
            <li>Chair: adjustable height, lumbar support, feet flat on floor</li>
            <li>Keyboard: wrists straight, elbows at 90°</li>
            <li>Lighting: no glare on screen, adequate room lighting</li>
            <li>Breaks: stand up and move every 30–60 minutes</li>
          </ul>
          <h4>Data Protection Law</h4>
          <p>Organisations that collect personal data must comply with data protection legislation (e.g., GDPR in Europe). Key principles:</p>
          <ul>
            <li>Data collected only for a specific, stated purpose</li>
            <li>Only minimum necessary data is collected</li>
            <li>Data kept secure and not shared without consent</li>
            <li>Individuals have the right to access and correct their data</li>
          </ul>
          <h4>Copyright Law</h4>
          <p>Software, music, images, and text are automatically protected by copyright. Violations include: copying software without licence, downloading pirated content, reproducing images without permission. Penalties can include fines and criminal charges.</p>
          <h4>Environmental Impact of IT</h4>
          <p>IT has significant environmental consequences: energy consumption of data centres, e-waste from discarded devices, toxic materials in circuit boards. <strong>Green IT</strong> practices: energy-efficient equipment, recycling old hardware, using cloud services to reduce physical infrastructure.</p>
        `
      }
    ],
"""

# ── MODULE 1 – Online Essentials ──────────────────────────────────────────────
lectures[1] = r"""    lecture: [
      {
        title: "L1 · Linux and the Ubuntu Operating System",
        body: `
          <h4>What is Linux?</h4>
          <p>Linux is an open-source operating system kernel created by <strong>Linus Torvalds in 1991</strong>. Unlike Windows or macOS, Linux is free, its source code is publicly available, and anyone can modify and distribute it. <strong>Ubuntu</strong> is the most popular desktop Linux distribution — it uses the Linux kernel combined with GNU tools and the Gnome desktop environment.</p>
          <h4>Why Linux for ICDL?</h4>
          <p>Linux is widely used in servers, supercomputers, and embedded systems. Understanding Linux gives you transferable skills in IT. The Bocconi ICDL exam specifically tests the Ubuntu Linux environment (Gnome desktop).</p>
          <h4>The Boot Process Explained</h4>
          <ol>
            <li>You press the power button</li>
            <li><strong>BIOS</strong> (stored in ROM) runs the Power-On Self Test (POST) — checks hardware is working</li>
            <li>BIOS loads the <strong>bootloader</strong> (GRUB in Linux) from the hard disk</li>
            <li>The bootloader loads the <strong>Linux kernel</strong> into RAM</li>
            <li>The kernel starts system services and the <strong>Gnome display manager</strong></li>
            <li>The login screen appears</li>
          </ol>
          <h4>Shutting Down Correctly</h4>
          <p>Always shut down via <strong>System → Log Out → Shut Down</strong>. Cutting power directly risks:</p>
          <ul>
            <li>Corrupting open files</li>
            <li>Damaging the file system journal</li>
            <li>Losing unsaved work</li>
          </ul>
        `
      },
      {
        title: "L2 · The Gnome Desktop Environment",
        body: `
          <h4>Gnome Desktop Layout</h4>
          <p>Gnome (GNU Network Object Model Environment) is the desktop environment in Ubuntu. It provides the visual interface you interact with.</p>
          <ul>
            <li><strong>Top Panel</strong> — contains the Applications menu, Places menu, System menu, clock, and system tray (network, volume, battery)</li>
            <li><strong>Desktop Area</strong> — the main workspace where windows open. Can have desktop icons and shortcuts</li>
            <li><strong>Bottom Panel</strong> — the taskbar showing open windows and running applications</li>
          </ul>
          <h4>Working with Windows</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Action</th><th style="padding:8px;text-align:left">How to do it</th><th style="padding:8px;text-align:left">Effect</th></tr>
            <tr><td style="padding:8px">Minimise</td><td style="padding:8px">Click _ button or taskbar button</td><td style="padding:8px">Hides window to taskbar; app keeps running</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Maximise</td><td style="padding:8px">Click □ button or double-click title bar</td><td style="padding:8px">Fills entire screen</td></tr>
            <tr><td style="padding:8px">Restore</td><td style="padding:8px">Click □ again or double-click title bar</td><td style="padding:8px">Returns to previous size</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Close</td><td style="padding:8px">Click X button or Alt+F4</td><td style="padding:8px">Closes the application</td></tr>
            <tr><td style="padding:8px">Move</td><td style="padding:8px">Drag the title bar</td><td style="padding:8px">Repositions window</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Resize</td><td style="padding:8px">Drag window edge or corner</td><td style="padding:8px">Changes window size</td></tr>
          </table>
          <h4>Desktop Customisation</h4>
          <ul>
            <li><strong>Wallpaper</strong> — right-click desktop → Change Desktop Background</li>
            <li><strong>Screen Resolution</strong> — System → Preferences → Screen Resolution (e.g., 1024×768, 1280×1024)</li>
            <li><strong>Screen Saver</strong> — System → Preferences → Screensaver</li>
            <li><strong>Date & Time</strong> — right-click the clock → Adjust Date & Time</li>
            <li><strong>Volume</strong> — click the speaker icon on the top panel</li>
            <li><strong>Keyboard Layout</strong> — System → Preferences → Keyboard → Layouts tab (add French, Arabic, etc.)</li>
          </ul>
        `
      },
      {
        title: "L3 · The Linux File System",
        body: `
          <h4>Linux File System Hierarchy</h4>
          <p>Linux uses a single directory tree starting from <strong>/ (the root)</strong>. Unlike Windows (which uses C:\\, D:\\), there are no drive letters. Everything is a file or directory branching from /.</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Directory</th><th style="padding:8px;text-align:left">Contents</th></tr>
            <tr><td style="padding:8px"><code>/</code></td><td style="padding:8px">Root — the top of the entire file system</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><code>/home</code></td><td style="padding:8px">User home directories (e.g., /home/zeynep)</td></tr>
            <tr><td style="padding:8px"><code>/etc</code></td><td style="padding:8px">System configuration files</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><code>/usr</code></td><td style="padding:8px">Installed applications and libraries</td></tr>
            <tr><td style="padding:8px"><code>/tmp</code></td><td style="padding:8px">Temporary files</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><code>/bin</code></td><td style="padding:8px">Essential system commands</td></tr>
          </table>
          <h4>File Naming in Linux</h4>
          <ul>
            <li>Linux is <strong>case-sensitive</strong>: Report.odt and report.odt are different files</li>
            <li>File names can contain letters, numbers, dots, underscores, hyphens</li>
            <li>Avoid spaces in file names (use underscores instead: my_report.odt)</li>
            <li>Hidden files start with a dot: .bashrc, .config</li>
          </ul>
          <h4>File Extensions in Linux</h4>
          <p>Unlike Windows, Linux does not rely on file extensions to determine file type — it reads the file content. However, extensions are still used as a convention:</p>
          <p>.odt (Writer), .ods (Calc), .odp (Impress), .jpg (image), .mp3 (audio), .pdf (document), .tar.gz (compressed archive)</p>
          <h4>The Trash (Recycle Bin)</h4>
          <p>Deleting a file in Gnome moves it to the Trash — it is NOT permanently deleted immediately. The file can be restored (right-click → Restore) until the Trash is emptied. Once emptied, the data is gone — it cannot be recovered through normal means.</p>
        `
      },
      {
        title: "L4 · File Management with Nautilus",
        body: `
          <h4>Nautilus File Manager</h4>
          <p>Nautilus is Ubuntu's default graphical file manager (equivalent to Windows Explorer). Access it via Places → Home Folder.</p>
          <h4>Essential File Operations</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Operation</th><th style="padding:8px;text-align:left">How (GUI)</th><th style="padding:8px;text-align:left">Keyboard</th></tr>
            <tr><td style="padding:8px">Copy</td><td style="padding:8px">Right-click → Copy</td><td style="padding:8px">Ctrl+C</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Cut (move)</td><td style="padding:8px">Right-click → Cut</td><td style="padding:8px">Ctrl+X</td></tr>
            <tr><td style="padding:8px">Paste</td><td style="padding:8px">Right-click → Paste</td><td style="padding:8px">Ctrl+V</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Delete</td><td style="padding:8px">Right-click → Move to Trash</td><td style="padding:8px">Delete key</td></tr>
            <tr><td style="padding:8px">Rename</td><td style="padding:8px">Right-click → Rename</td><td style="padding:8px">F2</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">New folder</td><td style="padding:8px">Right-click empty space → Create Folder</td><td style="padding:8px">Ctrl+Shift+N</td></tr>
            <tr><td style="padding:8px">Properties</td><td style="padding:8px">Right-click → Properties</td><td style="padding:8px">Alt+Enter</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Select all</td><td style="padding:8px">Edit → Select All</td><td style="padding:8px">Ctrl+A</td></tr>
          </table>
          <h4>Searching for Files</h4>
          <p>In Nautilus: click the Search button or press Ctrl+F. You can search by file name or content. The search is recursive — it looks in the current folder and all subfolders.</p>
          <h4>Managing Removable Media</h4>
          <ul>
            <li><strong>USB drives</strong> — automatically mount when plugged in; appear on the desktop and in Places. Always use <em>Eject</em> before removing to prevent data corruption.</li>
            <li><strong>Formatting</strong> — right-click the drive icon → Format. <strong>WARNING: This permanently erases ALL data on the drive.</strong> Formatting creates a fresh file system.</li>
          </ul>
        `
      },
      {
        title: "L5 · System Configuration & Printing",
        body: `
          <h4>Managing System Settings</h4>
          <p>All system settings are accessed via the <strong>System menu</strong> in the top panel:</p>
          <ul>
            <li><strong>System → Preferences</strong> — personal settings (wallpaper, screensaver, keyboard, mouse, display)</li>
            <li><strong>System → Administration</strong> — system-level settings (users, printing, software, network)</li>
          </ul>
          <h4>User Accounts</h4>
          <p>Linux is multi-user. Each user has their own home directory, settings, and permissions:</p>
          <ul>
            <li><strong>Standard user</strong> — limited permissions; cannot install system-wide software or change system files</li>
            <li><strong>Administrator (sudo)</strong> — can run commands with root privileges using the <code>sudo</code> command. In Ubuntu, the first user created during installation is automatically an administrator.</li>
          </ul>
          <h4>Installing and Removing Software</h4>
          <ul>
            <li><strong>Applications → Add/Remove</strong> — simple graphical package manager for common software</li>
            <li><strong>System → Administration → Synaptic Package Manager</strong> — full-featured package manager; shows all available packages</li>
            <li>Software in Ubuntu is installed from <strong>repositories</strong> — trusted servers maintained by Ubuntu. This ensures software is verified and virus-free.</li>
          </ul>
          <h4>Printing</h4>
          <p>Printing in Ubuntu:</p>
          <ul>
            <li><strong>File → Print (Ctrl+P)</strong> — opens the print dialog from any application</li>
            <li><strong>Print Preview</strong> — see the document before printing (File → Print Preview)</li>
            <li><strong>System → Administration → Printing</strong> — manage printers and print jobs</li>
            <li><strong>Print queue</strong> — shows pending, active, and completed print jobs. You can pause or cancel jobs.</li>
            <li><strong>Print to File</strong> — saves the output as a PDF instead of printing on paper</li>
          </ul>
          <h4>Screenshots</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Key</th><th style="padding:8px;text-align:left">Captures</th></tr>
            <tr><td style="padding:8px">Print Screen</td><td style="padding:8px">Entire screen</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Alt + Print Screen</td><td style="padding:8px">Active window only</td></tr>
          </table>
        `
      }
    ],
"""

# ── MODULE 2 – Word Processing ─────────────────────────────────────────────────
lectures[2] = r"""    lecture: [
      {
        title: "L1 · Introduction to OpenOffice Writer",
        body: `
          <h4>What is a Word Processor?</h4>
          <p>A word processor is software for creating, editing, formatting, and printing text documents. <strong>OpenOffice.org Writer</strong> is the free, open-source equivalent of Microsoft Word. It can open and save .doc and .docx files, making it compatible with Word users.</p>
          <h4>The Writer Interface</h4>
          <ul>
            <li><strong>Menu Bar</strong> — File, Edit, View, Insert, Format, Table, Tools, Window, Help</li>
            <li><strong>Standard Toolbar</strong> — New, Open, Save, Print, Undo, Redo, etc.</li>
            <li><strong>Formatting Toolbar</strong> — font name, size, bold, italic, underline, alignment buttons</li>
            <li><strong>Ruler</strong> — shows page margins and tab stops; drag to adjust indents</li>
            <li><strong>Status Bar</strong> — shows page count, word count, cursor position, zoom level</li>
            <li><strong>Document Area</strong> — the white page where you type</li>
          </ul>
          <h4>File Formats</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Extension</th><th style="padding:8px;text-align:left">Format</th><th style="padding:8px;text-align:left">Use case</th></tr>
            <tr><td style="padding:8px">.odt</td><td style="padding:8px">OpenDocument Text</td><td style="padding:8px">Default Writer format; open standard</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.doc / .docx</td><td style="padding:8px">Microsoft Word</td><td style="padding:8px">Sharing with Word users</td></tr>
            <tr><td style="padding:8px">.rtf</td><td style="padding:8px">Rich Text Format</td><td style="padding:8px">Universal compatibility across all word processors</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.txt</td><td style="padding:8px">Plain Text</td><td style="padding:8px">No formatting; maximum compatibility</td></tr>
            <tr><td style="padding:8px">.pdf</td><td style="padding:8px">Portable Document Format</td><td style="padding:8px">Final distribution; preserves layout exactly</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.html</td><td style="padding:8px">Web Page</td><td style="padding:8px">Publishing documents on the web</td></tr>
          </table>
        `
      },
      {
        title: "L2 · Text Editing Techniques",
        body: `
          <h4>Cursor Movement</h4>
          <p>Efficient text editing requires mastering cursor navigation without the mouse:</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Key</th><th style="padding:8px;text-align:left">Movement</th></tr>
            <tr><td style="padding:8px">Home / End</td><td style="padding:8px">Start / end of current line</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Ctrl+Home / Ctrl+End</td><td style="padding:8px">Start / end of document</td></tr>
            <tr><td style="padding:8px">Ctrl+Left / Ctrl+Right</td><td style="padding:8px">Jump one word left / right</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Page Up / Page Down</td><td style="padding:8px">Scroll one screen up / down</td></tr>
          </table>
          <h4>Selecting Text</h4>
          <ul>
            <li><strong>Click and drag</strong> — select any range of text</li>
            <li><strong>Shift + arrow keys</strong> — extend selection with keyboard</li>
            <li><strong>Double-click</strong> — selects one word</li>
            <li><strong>Triple-click</strong> — selects the entire paragraph</li>
            <li><strong>Ctrl+A</strong> — selects ALL content in the document</li>
          </ul>
          <h4>Delete vs Backspace</h4>
          <ul>
            <li><strong>Backspace</strong> — deletes the character to the LEFT of the cursor</li>
            <li><strong>Delete</strong> — deletes the character to the RIGHT of the cursor</li>
          </ul>
          <h4>Find and Replace (Ctrl+H)</h4>
          <p>Find and Replace is one of the most powerful editing tools:</p>
          <ul>
            <li>Finds every occurrence of a word in the document</li>
            <li>Can replace all at once (Replace All) or one at a time</li>
            <li>Useful for correcting repeated mistakes: e.g., replace all "colour" with "color"</li>
            <li><strong>Ctrl+F</strong> — opens Find only (no replace)</li>
          </ul>
          <h4>AutoCorrect and Spell Check</h4>
          <ul>
            <li><strong>AutoCorrect</strong> — fixes common errors as you type (teh → the, dont → don't). Customise via Tools → AutoCorrect Options.</li>
            <li><strong>Spell Check (F7)</strong> — checks the whole document. Misspelled words have a red underline; grammar issues have a green underline.</li>
            <li><strong>Right-click underlined word</strong> — suggests corrections</li>
          </ul>
        `
      },
      {
        title: "L3 · Character and Paragraph Formatting",
        body: `
          <h4>Character Formatting</h4>
          <p>Character formatting applies to individual characters or selected text. Access via the toolbar or Format → Character.</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Format</th><th style="padding:8px;text-align:left">Shortcut</th><th style="padding:8px;text-align:left">Purpose</th></tr>
            <tr><td style="padding:8px"><strong>Bold</strong></td><td style="padding:8px">Ctrl+B</td><td style="padding:8px">Emphasise important text</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><em>Italic</em></td><td style="padding:8px">Ctrl+I</td><td style="padding:8px">Titles, foreign words, light emphasis</td></tr>
            <tr><td style="padding:8px"><u>Underline</u></td><td style="padding:8px">Ctrl+U</td><td style="padding:8px">Important terms (avoid overuse)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Strikethrough</td><td style="padding:8px">Format → Character</td><td style="padding:8px">Show deleted or rejected text</td></tr>
            <tr><td style="padding:8px">Subscript</td><td style="padding:8px">Format → Character</td><td style="padding:8px">Chemical formulas: H₂O</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Superscript</td><td style="padding:8px">Format → Character</td><td style="padding:8px">Powers: x², footnotes</td></tr>
          </table>
          <p><strong>Font size</strong> is measured in <em>points (pt)</em>: 1 point ≈ 0.353 mm. 72pt ≈ 1 inch. Standard body text = 12pt. Headings = 14–18pt+.</p>
          <h4>Paragraph Formatting</h4>
          <p>Paragraph formatting applies to whole paragraphs. Place the cursor anywhere in the paragraph (no need to select all text).</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Alignment</th><th style="padding:8px;text-align:left">Shortcut</th><th style="padding:8px;text-align:left">Effect</th></tr>
            <tr><td style="padding:8px">Left</td><td style="padding:8px">Ctrl+L</td><td style="padding:8px">Text aligns to left margin (default for most text)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Centre</td><td style="padding:8px">Ctrl+E</td><td style="padding:8px">Text centred on the page (headings, titles)</td></tr>
            <tr><td style="padding:8px">Right</td><td style="padding:8px">Ctrl+R</td><td style="padding:8px">Text aligns to right margin (dates, addresses)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Justify</td><td style="padding:8px">Ctrl+J</td><td style="padding:8px">Text aligns to BOTH margins (books, newspapers)</td></tr>
          </table>
          <h4>Styles</h4>
          <p>Styles are named sets of formatting rules. Instead of manually formatting every heading, you apply the <strong>Heading 1</strong> style. Benefits:</p>
          <ul>
            <li>Consistency throughout the document</li>
            <li>Change the style definition once — all instances update automatically</li>
            <li>Required for automatic table of contents generation</li>
            <li>Access via the Styles and Formatting panel (F11)</li>
          </ul>
        `
      },
      {
        title: "L4 · Page Layout, Tables & Images",
        body: `
          <h4>Page Setup</h4>
          <p>Access via <strong>Format → Page</strong>:</p>
          <ul>
            <li><strong>Margins</strong> — space between the text and the edge of the page. Standard: 2.5 cm on all sides</li>
            <li><strong>Orientation</strong> — Portrait (taller than wide, standard) or Landscape (wider than tall, for wide tables)</li>
            <li><strong>Paper size</strong> — A4 (210×297 mm, standard in Europe), Letter (US), A3, etc.</li>
          </ul>
          <h4>Headers and Footers</h4>
          <p>Headers and footers repeat on every page. Typical content:</p>
          <ul>
            <li>Document title, chapter name, author (header)</li>
            <li>Page number, date, company name (footer)</li>
          </ul>
          <p>Insert via <strong>Insert → Header / Insert → Footer</strong>. Page numbers are added via <strong>Insert → Fields → Page Number</strong>.</p>
          <h4>Tables in Writer</h4>
          <p>Tables organise data in rows and columns. Insert via <strong>Table → Insert Table</strong>.</p>
          <ul>
            <li><strong>Tab</strong> — moves to the next cell; in the last cell, creates a new row</li>
            <li><strong>Shift+Tab</strong> — moves to the previous cell</li>
            <li><strong>Insert row/column</strong> — right-click in table → Insert Rows Above/Below or Insert Columns Before/After</li>
            <li><strong>Merge cells</strong> — select cells → Table → Merge Cells (creates a spanning header)</li>
            <li><strong>Split cells</strong> — Table → Split Cells</li>
            <li><strong>Table borders and shading</strong> — Table → Table Properties</li>
          </ul>
          <h4>Inserting Images</h4>
          <ul>
            <li>Insert → Picture → From File</li>
            <li>Resize by dragging handles (hold Shift to maintain proportions)</li>
            <li>Wrapping: Format → Picture → Wrapping — controls how text flows around the image (In Background, Wrap Through, Page Wrap, etc.)</li>
          </ul>
          <h4>Mail Merge</h4>
          <p>Mail merge creates personalised documents for many recipients by combining:</p>
          <ol>
            <li><strong>Main document</strong> — the letter template with merge fields (e.g., &lt;&lt;Name&gt;&gt;, &lt;&lt;Address&gt;&gt;)</li>
            <li><strong>Data source</strong> — a spreadsheet or database with the list of names and addresses</li>
          </ol>
          <p>Result: 100 personalised letters from one template. Access via Tools → Mail Merge Wizard.</p>
        `
      },
      {
        title: "L5 · Printing & Document Finalisation",
        body: `
          <h4>Print Preview</h4>
          <p><strong>File → Page Preview</strong> shows an exact representation of how the document will print. Check for:</p>
          <ul>
            <li>Correct page breaks (text not cut off awkwardly)</li>
            <li>Headers and footers appearing correctly</li>
            <li>Images positioned correctly</li>
            <li>Page numbering is correct</li>
          </ul>
          <h4>Print Settings (Ctrl+P)</h4>
          <ul>
            <li><strong>Printer selection</strong> — choose from installed printers or PDF writer</li>
            <li><strong>Page range</strong> — All pages, Current page, or specific pages (e.g., 1-3, 5, 7-9)</li>
            <li><strong>Copies</strong> — number of copies to print</li>
            <li><strong>Collate</strong> — when printing multiple copies, collate prints full sets (1-2-3, 1-2-3) rather than (1-1-1, 2-2-2, 3-3-3)</li>
            <li><strong>Print to File</strong> — saves as PostScript or PDF instead of physical printing</li>
          </ul>
          <h4>Non-Printing Characters</h4>
          <p>Press <strong>Ctrl+F10</strong> or View → Formatting Marks to show invisible characters:</p>
          <ul>
            <li>· (dot) = space</li>
            <li>→ = tab</li>
            <li>¶ = paragraph end (Enter key)</li>
          </ul>
          <p>Showing these helps diagnose layout problems caused by extra spaces, wrong tab stops, or missing paragraph breaks.</p>
          <h4>Saving Strategies</h4>
          <ul>
            <li><strong>Ctrl+S</strong> — save immediately (habit: save every few minutes)</li>
            <li><strong>AutoSave</strong> — Tools → Options → Load/Save → AutoSave interval (set to 5–10 minutes)</li>
            <li><strong>Save As (Ctrl+Shift+S)</strong> — create a copy in a different format or location. If you need to share with a Word user: File → Save As → format = .doc</li>
          </ul>
        `
      }
    ],
"""

# ── MODULE 3 – Spreadsheets ────────────────────────────────────────────────────
lectures[3] = r"""    lecture: [
      {
        title: "L1 · Spreadsheet Fundamentals",
        body: `
          <h4>What is a Spreadsheet?</h4>
          <p>A spreadsheet is software for organising, calculating, and analysing data in a grid of rows and columns. <strong>OpenOffice Calc</strong> is the free equivalent of Microsoft Excel. Spreadsheets are used for budgets, financial analysis, scientific data, charts, and much more.</p>
          <h4>Workbook and Worksheet Structure</h4>
          <ul>
            <li>A <strong>Workbook</strong> is the file (.ods). It contains one or more worksheets.</li>
            <li>A <strong>Worksheet</strong> (Sheet) is a single grid of rows and columns. Tabs at the bottom show sheet names (Sheet1, Sheet2...).</li>
            <li>A <strong>Cell</strong> is the intersection of a column and a row. Cell address = column letter + row number (e.g., B3 = column B, row 3).</li>
            <li>An <strong>Active cell</strong> is the currently selected cell, shown with a border and its address displayed in the Name Box.</li>
          </ul>
          <h4>Navigation</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Key</th><th style="padding:8px;text-align:left">Action</th></tr>
            <tr><td style="padding:8px">Arrow keys</td><td style="padding:8px">Move one cell in any direction</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Tab</td><td style="padding:8px">Move one cell to the right</td></tr>
            <tr><td style="padding:8px">Enter</td><td style="padding:8px">Confirm entry and move down</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Ctrl+Home</td><td style="padding:8px">Jump to cell A1</td></tr>
            <tr><td style="padding:8px">Ctrl+End</td><td style="padding:8px">Jump to last used cell</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Ctrl+G / Name Box</td><td style="padding:8px">Go to a specific cell address</td></tr>
          </table>
          <h4>Types of Data You Can Enter</h4>
          <ul>
            <li><strong>Text (labels)</strong> — automatically left-aligned. E.g., "Name", "January"</li>
            <li><strong>Numbers</strong> — automatically right-aligned. E.g., 1500, 3.14</li>
            <li><strong>Dates</strong> — stored as numbers; displayed as dates. E.g., 01/01/2024</li>
            <li><strong>Formulas</strong> — must start with = . Calculated values. E.g., =A1+B1</li>
          </ul>
        `
      },
      {
        title: "L2 · Formulas and Cell References",
        body: `
          <h4>Writing Formulas</h4>
          <p>Every formula starts with <strong>=</strong> (equals sign). Without it, Calc treats the entry as text.</p>
          <ul>
            <li><code>=A1+B1</code> — adds values in A1 and B1</li>
            <li><code>=A1*0.2</code> — multiplies A1 by 0.2 (20%)</li>
            <li><code>=B5-C5</code> — subtracts C5 from B5</li>
            <li><code>=(A1+B1)/2</code> — brackets control order of operations</li>
          </ul>
          <h4>Cell Reference Types</h4>
          <p>Understanding reference types is crucial for copying formulas correctly.</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Type</th><th style="padding:8px;text-align:left">Example</th><th style="padding:8px;text-align:left">Behaviour when copied</th></tr>
            <tr><td style="padding:8px"><strong>Relative</strong></td><td style="padding:8px">A1</td><td style="padding:8px">Both column and row adjust. Copy =A1 one row down → =A2</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Absolute</strong></td><td style="padding:8px">$A$1</td><td style="padding:8px">Both column and row are LOCKED. Always refers to A1 regardless of where copied.</td></tr>
            <tr><td style="padding:8px"><strong>Mixed (col locked)</strong></td><td style="padding:8px">$A1</td><td style="padding:8px">Column A locked; row adjusts when copied up/down</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Mixed (row locked)</strong></td><td style="padding:8px">A$1</td><td style="padding:8px">Row 1 locked; column adjusts when copied left/right</td></tr>
          </table>
          <p>Use absolute references when you need a formula to always point to the same cell — e.g., a tax rate stored in B1 that is referenced by all sales formulas: <code>=A5*$B$1</code></p>
          <h4>Common Error Messages</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Error</th><th style="padding:8px;text-align:left">Cause</th><th style="padding:8px;text-align:left">Fix</th></tr>
            <tr><td style="padding:8px">#DIV/0!</td><td style="padding:8px">Dividing by zero or empty cell</td><td style="padding:8px">Check divisor cell is not empty or zero</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">#REF!</td><td style="padding:8px">Invalid cell reference (e.g., deleted row)</td><td style="padding:8px">Update or re-enter the formula</td></tr>
            <tr><td style="padding:8px">#NAME?</td><td style="padding:8px">Unrecognised function name (typo)</td><td style="padding:8px">Check function spelling</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">#VALUE!</td><td style="padding:8px">Wrong data type (e.g., text in a numeric formula)</td><td style="padding:8px">Ensure referenced cells contain numbers</td></tr>
          </table>
        `
      },
      {
        title: "L3 · Functions in Depth",
        body: `
          <h4>What is a Function?</h4>
          <p>A function is a pre-built formula that performs a specific calculation. Syntax: <code>=FUNCTIONNAME(arguments)</code>. Arguments are separated by semicolons (;) in some locales or commas (,) in others.</p>
          <h4>Mathematical Functions</h4>
          <ul>
            <li><code>=SUM(A1:A10)</code> — adds all values from A1 to A10 (colon = range)</li>
            <li><code>=SUM(A1,B1,C1)</code> — adds only those three specific cells (comma = list)</li>
            <li><code>=AVERAGE(A1:A10)</code> — arithmetic mean</li>
            <li><code>=MIN(A1:A10)</code> — smallest value in range</li>
            <li><code>=MAX(A1:A10)</code> — largest value in range</li>
            <li><code>=ROUND(A1,2)</code> — rounds A1 to 2 decimal places</li>
          </ul>
          <h4>Counting Functions</h4>
          <ul>
            <li><code>=COUNT(A1:A20)</code> — counts cells containing <strong>numbers only</strong></li>
            <li><code>=COUNTA(A1:A20)</code> — counts all <strong>non-empty cells</strong> (any data type)</li>
            <li><code>=COUNTIF(A1:A20,"&gt;50")</code> — counts cells meeting a condition (greater than 50)</li>
            <li><code>=COUNTIF(A1:A20,"London")</code> — counts cells containing "London"</li>
          </ul>
          <h4>Logical Function: IF</h4>
          <p>The IF function is one of the most useful in spreadsheets:</p>
          <p style="font-family:monospace;background:var(--bg-card2);padding:10px;border-radius:6px">=IF(condition, value_if_true, value_if_false)</p>
          <p>Examples:</p>
          <ul>
            <li><code>=IF(B2&gt;=50, "Pass", "Fail")</code> — shows Pass if B2 ≥ 50, otherwise Fail</li>
            <li><code>=IF(C3&gt;1000, C3*0.1, 0)</code> — 10% discount if sales over 1000, otherwise 0</li>
          </ul>
          <h4>Text Functions</h4>
          <ul>
            <li><code>=A1&" "&B1</code> — concatenates (joins) text with a space between</li>
            <li><code>=TODAY()</code> — returns today's date (updates automatically)</li>
            <li><code>=NOW()</code> — returns current date and time</li>
          </ul>
        `
      },
      {
        title: "L4 · Charts and Data Visualisation",
        body: `
          <h4>Why Use Charts?</h4>
          <p>Charts transform raw numbers into visual representations that reveal trends, comparisons, and patterns that are difficult to spot in tables. A well-chosen chart makes data instantly understandable.</p>
          <h4>Choosing the Right Chart Type</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Chart Type</th><th style="padding:8px;text-align:left">Best for</th><th style="padding:8px;text-align:left">Example</th></tr>
            <tr><td style="padding:8px"><strong>Column/Bar</strong></td><td style="padding:8px">Comparing values across categories</td><td style="padding:8px">Sales by region, scores per student</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Line</strong></td><td style="padding:8px">Showing trends over time</td><td style="padding:8px">Monthly revenue, temperature over a year</td></tr>
            <tr><td style="padding:8px"><strong>Pie</strong></td><td style="padding:8px">Parts of a whole (proportions)</td><td style="padding:8px">Market share, budget breakdown</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Scatter</strong></td><td style="padding:8px">Relationship between two variables</td><td style="padding:8px">Height vs weight, study time vs marks</td></tr>
          </table>
          <p><strong>Pie chart tip:</strong> Only use for 2–6 categories. Too many slices make it unreadable. All slices must add to 100%.</p>
          <h4>Creating a Chart in Calc</h4>
          <ol>
            <li>Select the data range (including headings)</li>
            <li>Insert → Chart</li>
            <li>Choose chart type and click through the wizard</li>
            <li>Double-click the chart to enter edit mode; click outside to exit</li>
          </ol>
          <h4>Essential Chart Elements</h4>
          <ul>
            <li><strong>Title</strong> — describes what the chart shows</li>
            <li><strong>X-axis (horizontal)</strong> — categories or time periods</li>
            <li><strong>Y-axis (vertical)</strong> — values or quantities</li>
            <li><strong>Legend</strong> — identifies the data series (colour coding)</li>
            <li><strong>Data labels</strong> — values shown directly on bars/points</li>
          </ul>
        `
      },
      {
        title: "L5 · Data Management and Formatting",
        body: `
          <h4>Sorting Data</h4>
          <p>Data → Sort opens the sort dialog. You can sort by up to 3 columns. Always include/exclude the header row correctly (check "Range contains column labels").</p>
          <ul>
            <li><strong>Ascending</strong> — A to Z, 0 to 9, oldest to newest</li>
            <li><strong>Descending</strong> — Z to A, 9 to 0, newest to oldest</li>
          </ul>
          <h4>AutoFilter</h4>
          <p>Data → AutoFilter adds dropdown arrows to each column header. Click a dropdown to show only rows matching a criterion. The remaining rows are temporarily hidden (not deleted). Remove filter by selecting "All" in the dropdown.</p>
          <h4>Number Formatting</h4>
          <p>The underlying value in a cell does not change — only how it is displayed:</p>
          <ul>
            <li><strong>General</strong> — default; Calc decides how to display</li>
            <li><strong>Number</strong> — specify decimal places and thousand separators</li>
            <li><strong>Currency</strong> — adds £, $, € symbol and 2 decimal places</li>
            <li><strong>Percentage</strong> — multiplies by 100 and adds %. (0.75 displays as 75%)</li>
            <li><strong>Date</strong> — displays a date serial number as a date (DD/MM/YYYY, etc.)</li>
          </ul>
          <h4>Conditional Formatting</h4>
          <p>Format → Conditional → Condition. Examples:</p>
          <ul>
            <li>Colour cells red where value is below 0 (negative numbers)</li>
            <li>Colour cells green where value exceeds the target</li>
            <li>Highlight duplicate values</li>
          </ul>
          <h4>Freeze Panes</h4>
          <p>View → Freeze Rows and Columns. Click the cell BELOW and to the RIGHT of where you want to freeze. This keeps headers visible when scrolling through large datasets. E.g., click B2 to freeze row 1 (headers) and column A (labels).</p>
        `
      }
    ],
"""

# ── MODULE 5 – Presentation ───────────────────────────────────────────────────
lectures[5] = r"""    lecture: [
      {
        title: "L1 · Presentation Design Principles",
        body: `
          <h4>What Makes a Good Presentation?</h4>
          <p>A presentation is a communication tool — its purpose is to support the speaker, not replace them. The most common mistake is creating "death by PowerPoint" — slides packed with text that the presenter just reads aloud. The audience can read faster than you speak, so they will stop listening.</p>
          <h4>The 6×6 Rule</h4>
          <p>A widely-used guideline for slide content:</p>
          <ul>
            <li>Maximum <strong>6 bullet points</strong> per slide</li>
            <li>Maximum <strong>6 words</strong> per bullet point</li>
          </ul>
          <h4>Design Best Practices</h4>
          <ul>
            <li><strong>Contrast</strong> — use high contrast between text and background. Dark text on white or light text on dark. Never use yellow text on white.</li>
            <li><strong>Consistency</strong> — same fonts, colours, and layout throughout. Use the Slide Master to enforce this.</li>
            <li><strong>Simplicity</strong> — one idea per slide. Remove everything that is not essential.</li>
            <li><strong>Readable fonts</strong> — minimum 24pt for body text; 36pt+ for titles. Avoid decorative fonts for body text.</li>
            <li><strong>Images over words</strong> — a relevant image communicates faster than a paragraph of text.</li>
            <li><strong>Limit animations</strong> — use subtle, professional effects. Avoid flashy effects that distract from the content.</li>
          </ul>
          <h4>Presentation Structure</h4>
          <ol>
            <li><strong>Title slide</strong> — presentation title, presenter name, date, organisation</li>
            <li><strong>Agenda / Overview</strong> — tell the audience what you'll cover</li>
            <li><strong>Content slides</strong> — one key point per slide</li>
            <li><strong>Summary / Conclusion</strong> — recap key messages</li>
            <li><strong>Questions slide</strong> — invite audience questions</li>
          </ol>
        `
      },
      {
        title: "L2 · Working with Impress",
        body: `
          <h4>The Impress Interface</h4>
          <ul>
            <li><strong>Slides Panel (left)</strong> — thumbnail view of all slides for navigation and rearranging</li>
            <li><strong>Editing Area (centre)</strong> — the main slide editing canvas</li>
            <li><strong>Notes Panel (bottom)</strong> — speaker notes for the current slide</li>
            <li><strong>Properties Panel (right)</strong> — layouts, tables, and design options</li>
          </ul>
          <h4>View Modes</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">View</th><th style="padding:8px;text-align:left">Purpose</th><th style="padding:8px;text-align:left">Access</th></tr>
            <tr><td style="padding:8px"><strong>Normal</strong></td><td style="padding:8px">Main editing view</td><td style="padding:8px">View → Normal</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Outline</strong></td><td style="padding:8px">Review/edit all slide text in outline form</td><td style="padding:8px">View → Outline</td></tr>
            <tr><td style="padding:8px"><strong>Slide Sorter</strong></td><td style="padding:8px">Rearrange slide order by dragging thumbnails</td><td style="padding:8px">View → Slide Sorter</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Notes</strong></td><td style="padding:8px">Edit speaker notes for each slide</td><td style="padding:8px">View → Notes</td></tr>
            <tr><td style="padding:8px"><strong>Slide Show</strong></td><td style="padding:8px">Full screen presentation</td><td style="padding:8px">F5 (from start) / Shift+F5 (from current)</td></tr>
          </table>
          <h4>File Formats</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Extension</th><th style="padding:8px;text-align:left">Description</th></tr>
            <tr><td style="padding:8px">.odp</td><td style="padding:8px">OpenDocument Presentation — Impress native format</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.ppt / .pptx</td><td style="padding:8px">Microsoft PowerPoint format — for sharing with PowerPoint users</td></tr>
            <tr><td style="padding:8px">.pps</td><td style="padding:8px">PowerPoint Show — opens directly in slideshow mode (viewer-only)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.otp</td><td style="padding:8px">OpenDocument Presentation Template — design without content</td></tr>
          </table>
        `
      },
      {
        title: "L3 · Slide Master, Layouts & Design",
        body: `
          <h4>The Slide Master</h4>
          <p>The Slide Master is a <strong>template slide</strong> that controls the appearance of ALL slides in the presentation. Changes made to the Slide Master automatically apply to every slide. Access via <strong>View → Master → Slide Master</strong>.</p>
          <p>On the Slide Master you can set:</p>
          <ul>
            <li>Background (colour, gradient, image)</li>
            <li>Default fonts for titles and body text</li>
            <li>Logo or watermark position (appears on every slide)</li>
            <li>Colour scheme</li>
            <li>Footer, date, and slide number placeholders</li>
          </ul>
          <p>To return to normal editing: View → Normal.</p>
          <h4>Slide Layouts</h4>
          <p>A layout defines the arrangement of placeholder boxes on a slide. Common layouts:</p>
          <ul>
            <li><strong>Title Slide</strong> — large title + subtitle (first slide)</li>
            <li><strong>Title, Content</strong> — title + one content area (most common)</li>
            <li><strong>Two Content</strong> — title + two side-by-side content areas</li>
            <li><strong>Blank</strong> — no placeholders (fully custom)</li>
          </ul>
          <p>Change layout: Format → Layout, or right-click slide → Layout.</p>
          <h4>Design Templates</h4>
          <p>Format → Slide Design provides pre-built design templates with coordinated backgrounds, fonts, and colour palettes. Selecting one instantly transforms the visual style of all slides.</p>
        `
      },
      {
        title: "L4 · Animations and Transitions",
        body: `
          <h4>Slide Transitions</h4>
          <p>A <strong>transition</strong> is the visual effect when moving from one slide to the next during the slideshow. Access via <strong>Slide Show → Slide Transition</strong>.</p>
          <ul>
            <li><strong>Effect</strong> — choose from None, Fade, Wipe, Dissolve, Push, etc.</li>
            <li><strong>Speed</strong> — Slow, Medium, Fast</li>
            <li><strong>Advance slide</strong> — On mouse click (manual) or Automatically after N seconds</li>
            <li><strong>Apply to All Slides</strong> — applies the same transition throughout for consistency</li>
          </ul>
          <p><strong>Tip:</strong> Use the same simple transition for all slides. Avoid random mixed effects — they look unprofessional.</p>
          <h4>Object Animations</h4>
          <p>Animations control how individual objects (text boxes, images, shapes) appear, behave, or disappear on a slide. Access via <strong>Slide Show → Animation</strong>.</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Category</th><th style="padding:8px;text-align:left">Effect</th><th style="padding:8px;text-align:left">Examples</th></tr>
            <tr><td style="padding:8px"><strong>Entrance</strong></td><td style="padding:8px">Object appears on the slide</td><td style="padding:8px">Fly In, Fade, Zoom, Bounce</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Emphasis</strong></td><td style="padding:8px">Object changes while visible</td><td style="padding:8px">Spin, Grow, Change Colour</td></tr>
            <tr><td style="padding:8px"><strong>Exit</strong></td><td style="padding:8px">Object disappears from slide</td><td style="padding:8px">Fly Out, Fade Out, Collapse</td></tr>
          </table>
          <h4>Animation Timing</h4>
          <ul>
            <li><strong>On Click</strong> — plays when you click; useful for revealing bullet points one at a time</li>
            <li><strong>After Previous</strong> — plays automatically after the previous animation ends</li>
            <li><strong>With Previous</strong> — plays simultaneously with the previous animation</li>
          </ul>
        `
      },
      {
        title: "L5 · Delivering and Printing Presentations",
        body: `
          <h4>Running the Slideshow</h4>
          <ul>
            <li><strong>F5</strong> — start from the first slide</li>
            <li><strong>Shift+F5</strong> — start from the current slide</li>
            <li><strong>Click</strong> or <strong>Space/→ key</strong> — advance to next slide or trigger animation</li>
            <li><strong>← key</strong> — go back one slide</li>
            <li><strong>Escape</strong> — exit the slideshow</li>
            <li><strong>Right-click</strong> — menu with Go to Slide, End Show, etc.</li>
          </ul>
          <h4>Presenter View</h4>
          <p>When connected to a projector, you can use Presenter View — your screen shows the current slide, speaker notes, and next slide preview, while the audience only sees the current slide.</p>
          <h4>Printing Options</h4>
          <p>File → Print opens the print dialog. Key options:</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Print Type</th><th style="padding:8px;text-align:left">Description</th><th style="padding:8px;text-align:left">Use when</th></tr>
            <tr><td style="padding:8px"><strong>Slides</strong></td><td style="padding:8px">One full-size slide per page</td><td style="padding:8px">Producing posters or large prints</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Handouts</strong></td><td style="padding:8px">2, 3, 4, 6, or 9 slides per page</td><td style="padding:8px">Giving audience something to annotate</td></tr>
            <tr><td style="padding:8px"><strong>Notes</strong></td><td style="padding:8px">Slide + speaker notes below</td><td style="padding:8px">Presenter reference during delivery</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Outline</strong></td><td style="padding:8px">Text only — all titles and bullets</td><td style="padding:8px">Quick text review</td></tr>
          </table>
          <p><strong>Print in Greyscale</strong> — saves colour ink for drafts. Set in File → Print → Options → Greyscale.</p>
        `
      }
    ],
"""

# ── MODULE 6 – Online Collaboration ───────────────────────────────────────────
lectures[6] = r"""    lecture: [
      {
        title: "L1 · How the Internet Works",
        body: `
          <h4>The Internet Infrastructure</h4>
          <p>The Internet is a global network of interconnected computers and networks communicating via the <strong>TCP/IP protocol suite</strong>. No single organisation owns or controls the Internet.</p>
          <ul>
            <li><strong>Internet Backbone</strong> — the high-speed, high-capacity fibre optic cables and links that form the core of the Internet, connecting major cities and countries</li>
            <li><strong>ISP (Internet Service Provider)</strong> — companies that provide end-user access to the Internet (BT, Vodafone, Turkcell, etc.)</li>
            <li><strong>Router</strong> — a network device that forwards data packets between networks, directing traffic efficiently across the Internet</li>
            <li><strong>Modem</strong> — converts digital computer signals to the format used by your connection type (phone line, cable, fibre)</li>
          </ul>
          <h4>How Data Travels: Packets</h4>
          <p>Data is broken into small <strong>packets</strong> before transmission. Each packet travels independently through the network, potentially by different routes, and is reassembled at the destination. This is called <strong>packet switching</strong> — it is efficient and fault-tolerant (if one route fails, packets use another).</p>
          <h4>Key Internet Protocols</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Protocol</th><th style="padding:8px;text-align:left">Full name</th><th style="padding:8px;text-align:left">Purpose</th></tr>
            <tr><td style="padding:8px">HTTP</td><td style="padding:8px">HyperText Transfer Protocol</td><td style="padding:8px">Transfer web pages (unencrypted)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">HTTPS</td><td style="padding:8px">HTTP Secure</td><td style="padding:8px">Encrypted web pages (banking, shopping)</td></tr>
            <tr><td style="padding:8px">FTP</td><td style="padding:8px">File Transfer Protocol</td><td style="padding:8px">Upload/download files to/from servers</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">SMTP</td><td style="padding:8px">Simple Mail Transfer Protocol</td><td style="padding:8px">Send email</td></tr>
            <tr><td style="padding:8px">POP3</td><td style="padding:8px">Post Office Protocol v3</td><td style="padding:8px">Receive email (downloads to one device)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">IMAP</td><td style="padding:8px">Internet Message Access Protocol</td><td style="padding:8px">Receive email (syncs across all devices)</td></tr>
            <tr><td style="padding:8px">DNS</td><td style="padding:8px">Domain Name System</td><td style="padding:8px">Translates domain names to IP addresses</td></tr>
          </table>
        `
      },
      {
        title: "L2 · Web Browsers and URLs",
        body: `
          <h4>What is a Web Browser?</h4>
          <p>A web browser is software that retrieves, renders, and displays web pages. <strong>Firefox</strong> is the browser used in the ICDL exam. Others: Chrome, Edge, Safari, Opera.</p>
          <h4>Browser Interface Components</h4>
          <ul>
            <li><strong>Address bar</strong> — where you type URLs. Also shows security status (padlock)</li>
            <li><strong>Navigation buttons</strong> — Back, Forward, Reload, Home, Stop</li>
            <li><strong>Tab bar</strong> — open multiple pages simultaneously (Ctrl+T = new tab; Ctrl+W = close tab)</li>
            <li><strong>Bookmarks toolbar</strong> — quick access to saved pages</li>
            <li><strong>Status bar</strong> — shows loading progress and link URLs on hover</li>
          </ul>
          <h4>Understanding URLs</h4>
          <p>A URL (Uniform Resource Locator) is the complete address of a web page:</p>
          <p style="font-family:monospace;background:var(--bg-card2);padding:10px;border-radius:6px">https://www.bbc.co.uk/news/article.html</p>
          <ul>
            <li><strong>https://</strong> — protocol (secure)</li>
            <li><strong>www</strong> — subdomain</li>
            <li><strong>bbc.co.uk</strong> — domain name (registered, unique)</li>
            <li><strong>/news/article.html</strong> — path to the specific page</li>
          </ul>
          <h4>Domain Extensions</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Extension</th><th style="padding:8px;text-align:left">Type</th></tr>
            <tr><td style="padding:8px">.com</td><td style="padding:8px">Commercial organisation (most common)</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.org</td><td style="padding:8px">Non-profit organisation</td></tr>
            <tr><td style="padding:8px">.gov</td><td style="padding:8px">Government body</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.edu</td><td style="padding:8px">Educational institution</td></tr>
            <tr><td style="padding:8px">.co.uk</td><td style="padding:8px">UK commercial company</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">.ac.uk</td><td style="padding:8px">UK academic institution</td></tr>
          </table>
          <h4>Browser Security Indicators</h4>
          <ul>
            <li><strong>Padlock icon</strong> in address bar = HTTPS connection (encrypted)</li>
            <li><strong>Click the padlock</strong> to view the digital certificate and verify the website's identity</li>
            <li><strong>No padlock or "Not Secure"</strong> = HTTP only; data sent in plain text; never enter passwords or payment details</li>
          </ul>
        `
      },
      {
        title: "L3 · Email: Protocols, Composition & Etiquette",
        body: `
          <h4>How Email Works</h4>
          <ol>
            <li>You compose and send an email using your email client</li>
            <li>Your email client sends it to your mail server using <strong>SMTP</strong></li>
            <li>Your SMTP server routes it to the recipient's mail server</li>
            <li>The recipient retrieves it from their server using <strong>IMAP or POP3</strong></li>
          </ol>
          <h4>POP3 vs IMAP</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Feature</th><th style="padding:8px;text-align:left">POP3</th><th style="padding:8px;text-align:left">IMAP</th></tr>
            <tr><td style="padding:8px">Storage</td><td style="padding:8px">Downloaded to one device; removed from server</td><td style="padding:8px">Stays on server; synced to all devices</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Multi-device</td><td style="padding:8px">No — only one device sees emails</td><td style="padding:8px">Yes — phone, laptop, tablet all in sync</td></tr>
            <tr><td style="padding:8px">Offline access</td><td style="padding:8px">Yes (once downloaded)</td><td style="padding:8px">Requires internet to access server</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Best for</td><td style="padding:8px">Single device, limited server storage</td><td style="padding:8px">Multiple devices, modern use</td></tr>
          </table>
          <h4>Email Address Fields</h4>
          <ul>
            <li><strong>To</strong> — primary recipient(s)</li>
            <li><strong>CC (Carbon Copy)</strong> — secondary recipients who can see each other's addresses</li>
            <li><strong>BCC (Blind Carbon Copy)</strong> — recipients who are hidden from everyone else — they cannot see each other's addresses. Use for bulk emails to protect privacy.</li>
            <li><strong>Subject</strong> — brief description of the email content (always fill in — empty subjects look like spam)</li>
          </ul>
          <h4>Email Etiquette (Netiquette)</h4>
          <ul>
            <li>Use a clear, descriptive subject line</li>
            <li>Keep emails concise and professional</li>
            <li>Avoid ALL CAPITALS (considered shouting)</li>
            <li>Only use Reply All when everyone needs your response</li>
            <li>Compress large attachments before sending</li>
            <li>Add an email signature with your name and contact details</li>
            <li>Respond within 1–2 business days</li>
          </ul>
        `
      },
      {
        title: "L4 · Online Security and Privacy",
        body: `
          <h4>Cookies Explained</h4>
          <p>A cookie is a small text file a website stores on your computer. Types:</p>
          <ul>
            <li><strong>Session cookies</strong> — temporary; deleted when you close the browser (keep you logged in during a session)</li>
            <li><strong>Persistent cookies</strong> — stored on your drive; remember preferences across sessions</li>
            <li><strong>Third-party tracking cookies</strong> — placed by advertisers (not the site you're visiting); track your activity across multiple sites for targeted advertising</li>
          </ul>
          <p>You can clear cookies via browser settings. The GDPR requires websites to get your consent before placing non-essential cookies (hence the cookie banners).</p>
          <h4>Browser Cache</h4>
          <p>The cache stores copies of web pages, images, and scripts locally so they load faster on repeat visits. Problems occur when cached versions are outdated. Solution: hard refresh (Ctrl+Shift+R) or clear cache via browser settings.</p>
          <h4>HTTPS and Digital Certificates</h4>
          <p>HTTPS encrypts traffic between your browser and the server using <strong>TLS (Transport Layer Security)</strong>. This means even if someone intercepts your data packets, they cannot read the content. The encryption is verified by a <strong>Digital Certificate</strong> issued by a trusted Certificate Authority (CA) like DigiCert, Let's Encrypt, etc.</p>
          <h4>VPN (Virtual Private Network)</h4>
          <p>A VPN creates an encrypted "tunnel" over the public internet:</p>
          <ul>
            <li>All traffic is encrypted between your device and the VPN server</li>
            <li>Your real IP address is hidden</li>
            <li>Useful for: remote workers accessing company systems, security on public Wi-Fi, bypassing geographic restrictions</li>
          </ul>
        `
      },
      {
        title: "L5 · Cloud Services and Online Collaboration",
        body: `
          <h4>Cloud Computing</h4>
          <p>Cloud computing delivers computing services (storage, software, processing) over the internet instead of local hardware. You access them through a browser without installing anything.</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Service Type</th><th style="padding:8px;text-align:left">Description</th><th style="padding:8px;text-align:left">Examples</th></tr>
            <tr><td style="padding:8px"><strong>Cloud Storage</strong></td><td style="padding:8px">Store and access files from any device</td><td style="padding:8px">Google Drive, Dropbox, OneDrive</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Web-based apps</strong></td><td style="padding:8px">Run applications in the browser</td><td style="padding:8px">Google Docs, Office 365</td></tr>
            <tr><td style="padding:8px"><strong>VoIP</strong></td><td style="padding:8px">Voice calls over the internet</td><td style="padding:8px">Skype, WhatsApp, Zoom</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Social Networks</strong></td><td style="padding:8px">Connect and share with people</td><td style="padding:8px">LinkedIn, Instagram, X</td></tr>
          </table>
          <h4>Advantages and Disadvantages of Cloud Services</h4>
          <ul>
            <li>✅ Access from any device anywhere</li>
            <li>✅ Automatic backup and sync</li>
            <li>✅ Collaboration in real time (multiple users editing same document)</li>
            <li>✅ No hardware maintenance</li>
            <li>❌ Requires internet access</li>
            <li>❌ Privacy concerns — your data is on someone else's server</li>
            <li>❌ Dependent on provider — if they shut down, you may lose data</li>
            <li>❌ Ongoing subscription costs</li>
          </ul>
          <h4>VoIP (Voice over Internet Protocol)</h4>
          <p>VoIP converts voice into digital data packets and sends them over the internet. Much cheaper than traditional phone calls, especially for international calls. Requires: broadband internet, microphone, speakers. Examples: Skype, WhatsApp, Zoom, Teams, FaceTime.</p>
        `
      }
    ],
"""

# ── MODULE 7 – IT Security ────────────────────────────────────────────────────
lectures[7] = r"""    lecture: [
      {
        title: "L1 · Information Security Fundamentals",
        body: `
          <h4>Data vs Information</h4>
          <ul>
            <li><strong>Data</strong> — raw, unprocessed facts and figures (e.g., "25, London, 50000")</li>
            <li><strong>Information</strong> — data that has been processed and given context (e.g., "Ahmed, 25 years old, from London, earns £50,000")</li>
          </ul>
          <h4>The CIA Triad — Three Pillars of Information Security</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Pillar</th><th style="padding:8px;text-align:left">Meaning</th><th style="padding:8px;text-align:left">Threat example</th></tr>
            <tr><td style="padding:8px"><strong>Confidentiality</strong></td><td style="padding:8px">Data accessible only to authorised individuals</td><td style="padding:8px">Hacker reads customer database</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Integrity</strong></td><td style="padding:8px">Data is accurate, complete, and unaltered</td><td style="padding:8px">Attacker modifies financial records</td></tr>
            <tr><td style="padding:8px"><strong>Availability</strong></td><td style="padding:8px">Data accessible when needed by authorised users</td><td style="padding:8px">DDoS attack shuts down a website</td></tr>
          </table>
          <h4>Sources of Threats</h4>
          <ul>
            <li><strong>People (Insiders)</strong> — employees who accidentally or maliciously access, modify, or leak data. The most common source of breaches.</li>
            <li><strong>External attackers</strong> — hackers, organised crime, nation-state actors targeting systems for financial gain, espionage, or disruption</li>
            <li><strong>Natural / Physical events</strong> — fires, floods, power cuts, hardware failure — can destroy data if no backups exist</li>
            <li><strong>Cloud risks</strong> — storing data on third-party servers means you lose direct control. If the provider has a breach, your data is compromised.</li>
          </ul>
          <h4>Signs of Malware Infection</h4>
          <ul>
            <li>Browser homepage changed without your action</li>
            <li>Unexpected pop-up advertisements</li>
            <li>Programs starting automatically that you didn't open</li>
            <li>Computer performance dramatically slower than usual</li>
            <li>Emails sent from your account that you didn't write</li>
            <li>Files encrypted or inaccessible (ransomware)</li>
          </ul>
        `
      },
      {
        title: "L2 · Malware Types in Detail",
        body: `
          <h4>Complete Malware Classification</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Type</th><th style="padding:8px;text-align:left">How it spreads</th><th style="padding:8px;text-align:left">What it does</th></tr>
            <tr><td style="padding:8px"><strong>Virus</strong></td><td style="padding:8px">Attaches to files; spreads when infected files are shared</td><td style="padding:8px">Damages files, corrupts OS</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Worm</strong></td><td style="padding:8px">Self-propagates over networks automatically</td><td style="padding:8px">Consumes bandwidth, spreads other malware</td></tr>
            <tr><td style="padding:8px"><strong>Trojan Horse</strong></td><td style="padding:8px">Disguised as legitimate software</td><td style="padding:8px">Creates backdoor, steals data</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Ransomware</strong></td><td style="padding:8px">Email attachments, exploit kits</td><td style="padding:8px">Encrypts files; demands ransom</td></tr>
            <tr><td style="padding:8px"><strong>Spyware</strong></td><td style="padding:8px">Bundled with free software</td><td style="padding:8px">Records activity, sends to attacker</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Adware</strong></td><td style="padding:8px">Bundled with free software</td><td style="padding:8px">Displays unwanted ads, slows device</td></tr>
            <tr><td style="padding:8px"><strong>Keylogger</strong></td><td style="padding:8px">Installed by Trojan or physically</td><td style="padding:8px">Records keystrokes — steals passwords</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Rootkit</strong></td><td style="padding:8px">Exploits OS vulnerabilities</td><td style="padding:8px">Hides in OS; grants attacker admin access</td></tr>
            <tr><td style="padding:8px"><strong>Botnet</strong></td><td style="padding:8px">Worms or drive-by downloads</td><td style="padding:8px">Turns device into "zombie" for spam/DDoS</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Backdoor</strong></td><td style="padding:8px">Left by Trojans or developers</td><td style="padding:8px">Secret entry bypassing authentication</td></tr>
          </table>
          <h4>How Malware Enters Systems</h4>
          <ul>
            <li>Opening email attachments from unknown senders (.exe, .bat, .zip)</li>
            <li>Downloading software from untrusted websites</li>
            <li>Using infected USB drives (autorun)</li>
            <li>Visiting compromised websites (drive-by download)</li>
            <li>Exploiting unpatched software vulnerabilities</li>
          </ul>
          <h4>Protection Measures</h4>
          <ul>
            <li>Install reputable antivirus/antimalware software and keep it updated</li>
            <li>Keep the OS and all software updated (patches fix known vulnerabilities)</li>
            <li>Never open unexpected email attachments</li>
            <li>Download software only from official sources</li>
            <li>Regular backups to recover from ransomware without paying</li>
          </ul>
        `
      },
      {
        title: "L3 · Hacking and Social Engineering",
        body: `
          <h4>Types of Hackers</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Type</th><th style="padding:8px;text-align:left">Description</th><th style="padding:8px;text-align:left">Legal status</th></tr>
            <tr><td style="padding:8px"><strong>Black Hat (Cracker)</strong></td><td style="padding:8px">Malicious; attacks for personal gain or damage</td><td style="padding:8px">Illegal</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>White Hat</strong></td><td style="padding:8px">Ethical hacker hired to test security (penetration testing)</td><td style="padding:8px">Legal (with permission)</td></tr>
            <tr><td style="padding:8px"><strong>Grey Hat</strong></td><td style="padding:8px">Finds vulnerabilities without consent; no malicious intent</td><td style="padding:8px">Legally ambiguous</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px"><strong>Script Kiddie</strong></td><td style="padding:8px">Uses others' tools without understanding; no skill</td><td style="padding:8px">Often illegal</td></tr>
          </table>
          <h4>Social Engineering — Attacking Humans, Not Systems</h4>
          <p>Social engineering exploits human psychology rather than technical vulnerabilities. No matter how secure the technology, humans can be manipulated. Types:</p>
          <ul>
            <li><strong>Phishing</strong> — mass fake emails/websites impersonating banks, government, or trusted brands. Aim: steal credentials or install malware. Signs: unexpected urgency, poor grammar, link domain differs from the stated organisation.</li>
            <li><strong>Spear Phishing</strong> — targeted phishing; personalised with victim's name and details. More convincing and dangerous.</li>
            <li><strong>Shoulder Surfing</strong> — physically watching someone type a password or PIN. Can use binoculars or camera from a distance.</li>
            <li><strong>Pretexting</strong> — fabricating a scenario (e.g., "I'm from IT support — I need your password to fix your account"). Exploits trust and authority.</li>
            <li><strong>Information Diving</strong> — searching rubbish bins for discarded documents containing passwords, account numbers, or personal data. Prevention: shred sensitive documents.</li>
          </ul>
          <h4>Identity Theft Techniques</h4>
          <ul>
            <li><strong>Skimming</strong> — hidden device on ATM or card reader clones your card's magnetic stripe data. Always check ATMs for unusual attachments.</li>
            <li><strong>Pharming</strong> — DNS cache poisoning redirects legitimate URLs to fake sites. The URL looks correct but you are on a fake server. Only the digital certificate reveals the deception.</li>
          </ul>
        `
      },
      {
        title: "L4 · Passwords, Authentication & Encryption",
        body: `
          <h4>What Makes a Strong Password?</h4>
          <p>Passwords are the first line of defence. Most attacks use automated tools that try millions of combinations per second (brute force) or use databases of known passwords (dictionary attacks).</p>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Requirement</th><th style="padding:8px;text-align:left">Why it matters</th></tr>
            <tr><td style="padding:8px">At least 8 characters (14+ very strong)</td><td style="padding:8px">Longer = exponentially more combinations to try</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Mix uppercase, lowercase, numbers, symbols</td><td style="padding:8px">Increases the character set size, defeating dictionary attacks</td></tr>
            <tr><td style="padding:8px">No real words, names, or dates</td><td style="padding:8px">Dictionary attacks try all common words first</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">Unique per account</td><td style="padding:8px">A breach of one site doesn't compromise others</td></tr>
            <tr><td style="padding:8px">Change regularly</td><td style="padding:8px">Limits damage from unknown past breaches</td></tr>
          </table>
          <h4>Multi-Factor Authentication (MFA)</h4>
          <p>MFA requires two or more of these factors:</p>
          <ul>
            <li><strong>Something you know</strong> — password, PIN</li>
            <li><strong>Something you have</strong> — OTP token, smartphone, smart card</li>
            <li><strong>Something you are</strong> — fingerprint, iris scan, face recognition (biometrics)</li>
          </ul>
          <p>Even if a password is stolen, the attacker cannot log in without the second factor.</p>
          <h4>OTP (One-Time Password)</h4>
          <p>An OTP is valid for only 30 seconds to 10 minutes. Generated by an authenticator app (Google Authenticator, Microsoft Authenticator), hardware token, or sent via SMS. Used in banking and high-security systems.</p>
          <h4>Encryption</h4>
          <p>Encryption uses a mathematical algorithm and a key to scramble data:</p>
          <ul>
            <li><strong>Symmetric encryption</strong> — same key for encrypting and decrypting (fast; key distribution is a challenge)</li>
            <li><strong>Asymmetric encryption (Public Key)</strong> — two keys: public key (anyone can encrypt) + private key (only owner can decrypt). Used in HTTPS, email signing.</li>
          </ul>
          <p>If you lose the encryption key, you permanently lose access to the data — even the service provider cannot recover it.</p>
        `
      },
      {
        title: "L5 · Network Security and GDPR",
        body: `
          <h4>Firewall</h4>
          <p>A firewall monitors and filters all incoming and outgoing network traffic based on predefined security rules. It can be:</p>
          <ul>
            <li><strong>Hardware firewall</strong> — a physical device (e.g., a router with firewall capability) protecting an entire network</li>
            <li><strong>Software firewall</strong> — installed on individual computers (Windows Defender Firewall, etc.)</li>
          </ul>
          <p><strong>Limitations:</strong> A firewall cannot stop attacks that originate from inside the network (malicious employees) or threats that travel through permitted ports (e.g., malicious email attachments).</p>
          <h4>Wireless Security Standards</h4>
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem">
            <tr style="background:var(--bg-card2)"><th style="padding:8px;text-align:left">Standard</th><th style="padding:8px;text-align:left">Year</th><th style="padding:8px;text-align:left">Security level</th></tr>
            <tr><td style="padding:8px">Open (no encryption)</td><td style="padding:8px">—</td><td style="padding:8px">None — anyone can intercept all traffic</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">WEP</td><td style="padding:8px">1999</td><td style="padding:8px">Broken — crackable in minutes; do not use</td></tr>
            <tr><td style="padding:8px">WPA</td><td style="padding:8px">2003</td><td style="padding:8px">Improved but has known vulnerabilities</td></tr>
            <tr style="background:var(--bg-card2)"><td style="padding:8px">WPA2</td><td style="padding:8px">2004</td><td style="padding:8px">Current standard — considered fully secure</td></tr>
          </table>
          <h4>GDPR Key Principles</h4>
          <p>The General Data Protection Regulation (GDPR) — effective in the EU since 2018 — governs how personal data must be handled:</p>
          <ul>
            <li><strong>Transparency</strong> — individuals must be told how their data is collected and used</li>
            <li><strong>Legitimacy (Purpose limitation)</strong> — data can only be collected for a specific, stated, lawful purpose; cannot be used beyond that purpose</li>
            <li><strong>Proportionality (Data minimisation)</strong> — collect only the minimum data necessary; security measures proportional to risk</li>
            <li><strong>Data Controller</strong> — the organisation that determines the purpose and means of data processing; legally responsible for compliance</li>
            <li><strong>Data Subject rights</strong> — right to be informed, access data, correct inaccuracies, object to processing, request deletion ("right to be forgotten")</li>
          </ul>
          <h4>Backups — Your Last Line of Defence</h4>
          <p>The <strong>3-2-1 backup rule</strong>:</p>
          <ul>
            <li>Keep <strong>3</strong> copies of your data</li>
            <li>On <strong>2</strong> different storage types (e.g., HDD and cloud)</li>
            <li>With <strong>1</strong> copy stored offsite (protects against fire, flood)</li>
          </ul>
          <p>Test your backups regularly — a backup you have never tested is an untested backup.</p>
        `
      }
    ],
"""

# ── INJECT LECTURE DATA INTO EACH MODULE ─────────────────────────────────────
# Each module's flashcards section starts with a unique marker
# We insert lecture data BEFORE the flashcards key

module_flashcard_markers = {
    0: '    flashcards: [\n      {f:"What is hardware?',
    1: '    flashcards: [\n      {f:"What happens during the computer boot process?',
    2: '    flashcards: [\n      {f:"What is the default file extension for OpenOffice Writer',
    3: '    flashcards: [\n      {f:"What is a cell address and give an example?',
    5: '    flashcards: [\n      {f:"What is the default file extension for OpenOffice Impress?',
    6: '    flashcards: [\n      {f:"What is the difference between the Internet and the WWW?',
    7: '    flashcards: [\n      {f:"What are the three pillars of information security?',
}

count = 0
for mod_id, lecture_data in lectures.items():
    marker = module_flashcard_markers.get(mod_id)
    if not marker:
        print(f"No marker for module {mod_id}")
        continue
    idx = content.find(marker)
    if idx == -1:
        print(f"Marker NOT FOUND for module {mod_id}: {marker[:60]}")
        continue
    content = content[:idx] + lecture_data + content[idx:]
    count += 1
    print(f"OK: Inserted lecture for module {mod_id}")

print(f"\nTotal modules updated: {count}/7")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Wrote icdl_study_app.html")

import shutil
shutil.copy(path, "C:/Users/Windows 10/Desktop/r ta/index.html")
print("Copied to index.html")
