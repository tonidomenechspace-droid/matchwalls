class DragHorizontalScroll {
  constructor(DOMElement) {
    this.slider = document.querySelector(DOMElement)
    this.mouseDown = false
    this.startX = 0
    this.scrollLeft = 0

    this.touchStartX = 0
    this.touchStartScrollLeft = 0

    this.slider.addEventListener('mousemove', this.move.bind(this), false)
    this.slider.addEventListener(
      'mousedown',
      this.startDragging.bind(this),
      false
    )
    this.slider.addEventListener('mouseup', this.stopDragging.bind(this), false)
    this.slider.addEventListener(
      'mouseleave',
      this.stopDragging.bind(this),
      false
    )

    this.slider.addEventListener(
      'touchstart',
      this.startTouchDragging.bind(this),
      false
    )
    this.slider.addEventListener(
      'touchend',
      this.stopTouchDragging.bind(this),
      false
    )
    this.slider.addEventListener('touchmove', this.moveTouch.bind(this), false)
  }

  startDragging(e) {
    this.mouseDown = true
    this.startX = e.pageX - this.slider.offsetLeft
    this.scrollLeft = this.slider.scrollLeft
  }

  stopDragging(e) {
    this.mouseDown = false
  }

  move(e) {
    e.preventDefault()
    if (!this.mouseDown) return
    const x = e.pageX - this.slider.offsetLeft
    const scroll = x - this.startX
    this.slider.scrollLeft = this.scrollLeft - scroll

    // Save the current scroll position to localStorage
    localStorage.setItem('sliderScrollPosition', this.slider.scrollLeft)
  }

  startTouchDragging(e) {
    this.touchStartX = e.touches[0].pageX - this.slider.offsetLeft
    this.touchStartScrollLeft = this.slider.scrollLeft
  }

  stopTouchDragging(e) {
    // No action needed for touch end
  }

  moveTouch(e) {
    e.preventDefault()
    const touchX = e.touches[0].pageX - this.slider.offsetLeft
    const touchScroll = touchX - this.touchStartX
    this.slider.scrollLeft = this.touchStartScrollLeft - touchScroll

    // Save the current scroll position to localStorage
    localStorage.setItem('sliderScrollPosition', this.slider.scrollLeft)
  }
}



class CustomizerDialog extends HTMLElement {
  constructor() {
    super()
    this.currentPrice = null
    this.currentPriceCompare = null
    this.currentVariant = null
    this.measure = ''
    this.dimensions = 0

    this.width = 0
    this.height = 0

    // All measures have 1m as base unit
    this.surface = {
      m: 1,
      ft: 10.764,
      cm: 10000,
      in: 1550
    }

    this.elems = {
      form: null,
      dialogElem: null,
      cancelButtons: null,
      openButton: null,
      quantityInput: null,
      radioInputs: null,
      numberInputs: null,
      price: null,
      dimensions: null,
      idInput: null,
      rolls: null
    }

    this.totalQuantity = 0
    this.elems.rolls = null
  }

  connectedCallback() {
    // Variables
    const surface = Number(this.getAttribute('data-surface'))
    console.log(surface)
    if (surface) {
      this.surface.m = surface
      this.surface.ft = surface * 10.764
      this.surface.cm = surface * 10000
      this.surface.in = surface * 1550
    }
    this.elems.length = this.querySelector('button[data-action="length"]')
    this.elems.lengthLinesElem = this.querySelector('.length-lines')
    this.elems.form = this.querySelector('form')
    this.elems.idInput = this.querySelector('input[name=id]')
    this.elems.dialogElem = this.querySelector('dialog')
    this.elems.openButton = this.querySelector('[open-modal]')
    this.elems.cancelButtons = this.querySelectorAll('[close-modal]')
    this.elems.numberInputs = this.querySelectorAll('input[type=number]')
    this.elems.radioInputs = this.querySelectorAll('input[type=radio]')
    this.elems.quantityInput = this.querySelector('input[name=quantity]')
    this.elems.price = this.querySelector('.final-price')
    this.elems.priceCompare = this.querySelector('.compare-final-price')
    this.elems.dimensions = this.querySelector('.total-surface')
    this.elems.rolls = this.querySelector('.rolls-quantity')
    this.pdfButton = document.querySelector('#downloadpdf');
    if (this.pdfButton) {
      window.addEventListener('load', () => {
        this.pdfButton.addEventListener('click', this.generatePDF.bind(this));
      });
    }
    // Listeners
    this.elems.openButton.addEventListener('click', this.openDialog.bind(this))
    this.elems.cancelButtons.forEach((elem) => {
      elem.addEventListener('click', this.closeDialog.bind(this))
    })
    this.elems.numberInputs.forEach((input) => {
      input.addEventListener('input', this.onInputNumberChange.bind(this))
    })
    this.elems.radioInputs.forEach((input) => {
      if (input.checked) this.measure = input.value
      input.addEventListener('change', this.onRadioChange.bind(this))
    })
    this.elems.form.addEventListener('submit', this.closeDialog.bind(this))
    this.extendSetup()
    this.update()
  }
  openDialog() {
    this.elems.dialogElem.showModal()
    this.update()
  }

  closeDialog() {
    this.elems.dialogElem.close()
  }

  onInputNumberChange(e) {
    const max = Number(e.target.max)
    const min = Number(e.target.min)
    const val = Number(e.target.value)

    if (val > max) {
      e.target.value = max
    } else if (val < min) {
      // e.target.value = min
    }
    this.update()
  }

  onRadioChange(e) {
    const unitSpans = document.querySelectorAll('.unit-form-control');
    console.log("this.meaure: ", this.measure)
    const newUnit = this.measure === 'ft' ? window.unitsTranslations.meter : window.unitsTranslations.feet;
    unitSpans.forEach(span => {
      span.textContent = newUnit;
    });
    this.measure = e.target.value
    this.update()
  }

  update() {
    this.updateValues()
    this.updateUI()
  }

  // This method is empty but required. The idea is that each child class can extend elements not present in the current constructor on the connectedCallback without modifying it.
  extendSetup() { }

  updateValues() {
    this.width = Number(this.elems.numberInputs[0].value)
    this.height = Number(this.elems.numberInputs[1].value)

    this.dimensions = Math.round(this.height * this.width * 100) / 100
    this.totalQuantity = Math.ceil(this.dimensions / this.surface[this.measure])
    this.elems.quantityInput.value = this.totalQuantity

    const id = document.querySelector(
      'input[name="id"]:not([customizer-input])'
    ).value

    document.querySelector(
      'input[name="quantity"]:not([customizer-input])'
    ).value = this.totalQuantity

    this.elems.idInput.value = id
    this.currentPrice = window.product.variants.find(
      (variant) => variant.id == id
    ).price
    this.currentPriceCompare = window.product.variants.find(
      (variant) => variant.id == id
    ).compare_at_price
  }
  updateUI() {
    const totalPrice = this.totalQuantity * (this.currentPrice / 100)
    console.log(" total Price: ", totalPrice)
    const currencySymbol = `${window.Shopify.currency.active} `
    console.log("window.Shopify.currency.active: ", window.Shopify)

    this.elems.dimensions.textContent = this.dimensions + this.measure
    this.elems.rolls.textContent = this.totalQuantity
    this.elems.price.textContent = `${currencySymbol}${totalPrice.toFixed(2)}`
    const totalPriceCompare = this.totalQuantity * (this.currentPriceCompare / 100)
    this.elems.priceCompare.textContent = `${currencySymbol}${totalPriceCompare.toFixed(2)}`;
    // Calculate the percentage discount and round it to the nearest whole number
    let discountPercentage = 0;
    if (totalPriceCompare > totalPrice) {
      discountPercentage = Math.round(((totalPriceCompare - totalPrice) / totalPriceCompare) * 100);
    }

    // Display the discount percentage if there's any discount
    if (discountPercentage > 0) {
      const discountElement = document.querySelector(".discount-percentage");
      discountElement.textContent = `-${discountPercentage}% `;
    }
    console.log("totalPriceCompare: ", totalPriceCompare)
  }
  generatePDF() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
      event: 'stimulation_download'
    });
    console.log("window.product: ", window.product);
    console.log("this.elemes.form: ", this.elems.form);

    const variantIdInput = this.elems.form.querySelector('input[name="id"]').value;
    console.log("here is the variant Input: ", variantIdInput);

    const productVariants = window.product.variants;
    console.log("productVariants: ", productVariants);

    const selectedVariant = productVariants.find(variant => variant.id == variantIdInput);

    if (selectedVariant) {
      console.log("Selected Variant Title: ", selectedVariant.title);
    } else {
      console.error("Variant not found for ID:", variantIdInput);
    }

    // Show spinner and overlay before PDF generation starts
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('spinnerOverlay').style.display = 'block';

    console.log('generatePDF called!');

    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const pageWidth = doc.internal.pageSize.getWidth();
    const pageHeight = doc.internal.pageSize.getHeight();

    const titleProduct = document.querySelector("#product-title");
    const title = titleProduct ? titleProduct.innerHTML.trim() : "Title not found";

    const skProduct = document.querySelector("#product-sku");
    const sku = skProduct ? skProduct.innerHTML.trim() : "SKU not found";

    const quaProduct = document.querySelector(".variant-picker__option button span");
    const quality = selectedVariant.title;

    const finalPrice = document.querySelector(".customizer__body .final-price").textContent;
    const currencySymbol = "EUR"; // Change this if needed

    const widthCm = this.width || 0;
    const heightCm = this.height || 0;
    const widthInch = (widthCm * 0.393701).toFixed(2);
    const heightInch = (heightCm * 0.393701).toFixed(2);
    const surfaceM2 = (widthCm * heightCm / 10000).toFixed(2);
    const surfaceFt2 = (surfaceM2 * 10.7639).toFixed(2);

    const textTitle = `Producto: ${title} | Referencia: ${sku}`;
    const textQuality = `Calidad del papel: ${quality}`;

    const textPrice = `Precio: ${finalPrice}`;
    const dimensionsText = `Medidas: ${widthCm} cm x ${heightCm} cm (${surfaceM2} m²) | ${widthInch} in x ${heightInch} in (${surfaceFt2} ft²)`;
    const surfaceText = `${surfaceM2} m² - ${surfaceFt2} ft²`;

    this.captureFrameImage().then((blob) => {
      const reader = new FileReader();

      reader.onload = function (event) {
        const imgData = event.target.result;

        const imageSectionHeight = pageHeight * 0.40;
        const maxImgHeight = imageSectionHeight * 0.70;
        const imgProps = doc.getImageProperties(imgData);
        let imgWidth = pageWidth * 0.9;
        let imgHeight = (imgProps.height * imgWidth) / imgProps.width;
        let imgXPosition = (pageWidth - imgWidth) / 2;

        if (imgHeight > maxImgHeight) {
          imgHeight = maxImgHeight;
          imgWidth = (imgProps.width * imgHeight) / imgProps.height;
          imgXPosition = (pageWidth - imgWidth) / 2;
        }
        const imgYPosition = 20;

        doc.setFontSize(14);
        doc.setTextColor(0, 0, 0);
        doc.text(surfaceText, pageWidth / 2, imgYPosition - 5, { align: 'center' });

        const adjustedImgYPosition = imgYPosition + 5;

        doc.addImage(imgData, 'PNG', imgXPosition, adjustedImgYPosition, imgWidth, imgHeight);

        doc.setLineWidth(0.5);
        const marginHeight = -20;
        const margin = 0;
        doc.line(imgXPosition - 4, adjustedImgYPosition, imgXPosition - 4, adjustedImgYPosition + imgHeight);
        doc.line(imgXPosition + imgWidth, adjustedImgYPosition, imgXPosition + imgWidth, adjustedImgYPosition + imgHeight);
        doc.line(imgXPosition, adjustedImgYPosition + 4 + imgHeight, imgXPosition + imgWidth, adjustedImgYPosition + imgHeight + 4);

        doc.setFontSize(10);
        doc.setTextColor(0, 0, 0);
        doc.text(`${heightCm} cm / ${heightInch} in`, imgXPosition - marginHeight, adjustedImgYPosition + (imgHeight / 2), { align: 'right', angle: 90 });
        doc.text(`${widthCm} cm / ${widthInch} in`, imgXPosition + imgWidth / 2, adjustedImgYPosition + imgHeight + margin + 10, { align: 'center' });

        const productInfoYPosition = adjustedImgYPosition + imgHeight + 20;
        doc.text(textTitle, 10, productInfoYPosition);
        doc.text(textQuality, 10, productInfoYPosition + 10);
        doc.text(dimensionsText, 10, productInfoYPosition + 20);
        doc.text(textPrice, 10, productInfoYPosition + 30);

        const legalInfoYPosition = productInfoYPosition + 50;
        const legalOne = window.customizer.legalone || "Legal text 1 not found";
        const legalTwo = window.customizer.legaltwo || "Legal text 2 not found";
        const legalTwoLines = doc.splitTextToSize(legalTwo, pageWidth - 20);
        const legalOneLines = doc.splitTextToSize(legalOne, pageWidth - 20);

        doc.setTextColor(0, 0, 0);
        doc.text(legalOneLines, 10, legalInfoYPosition, { maxWidth: pageWidth - 20 });
        doc.text(legalTwoLines, 10, legalInfoYPosition + 20, { maxWidth: pageWidth - 20 });

        // Select the logo from the DOM using querySelector
        const logoElement = document.querySelector('.header__logo-image');
        if (logoElement) {
          const logoSrc = logoElement.getAttribute('src');

          // Convert SVG to PNG using a canvas element
          const logoImg = new Image();
          logoImg.src = logoSrc;
          logoImg.onload = function () {
            const canvas = document.createElement('canvas');
            canvas.width = logoImg.width;
            canvas.height = logoImg.height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(logoImg, 0, 0);
            const logoDataUrl = canvas.toDataURL('image/png');  // Convert to PNG format

            const footerImageHeight = 15;  // Adjust as needed
            const footerImageYPosition = pageHeight - footerImageHeight - 10;  // 10 units margin from the bottom
            const logoWidth = (logoImg.width / logoImg.height) * footerImageHeight; // Maintain aspect ratio

            doc.addImage(logoDataUrl, 'PNG', (pageWidth - logoWidth) / 2, footerImageYPosition, logoWidth, footerImageHeight);
            doc.save("customizer-summary.pdf");

            // Hide spinner and overlay after PDF is saved
            document.getElementById('loadingSpinner').style.display = 'none';
            document.getElementById('spinnerOverlay').style.display = 'none';
          };
        } else {
          console.error('Logo image not found');
        }
      };

      reader.readAsDataURL(blob);
    }).catch(error => {
      console.error('Error capturing frame image:', error);

      // Hide spinner and overlay in case of error
      document.getElementById('loadingSpinner').style.display = 'none';
      document.getElementById('spinnerOverlay').style.display = 'none';
    });
  }












}

customElements.define('rolls-calculator', CustomizerDialog)

class ProductCustomizer extends CustomizerDialog {
  constructor() {
    super();
    this.isReplicated = this.getAttribute('replicate-product') === 'true';
    this.pixels = {
      cm: 37.795275591, // 1 cm to pixels
      in: 96,          // 1 inch to pixels
      feet: 1152       // 1 foot to pixels (96 * 12)
    };
    this.maxWidth = 0;
    this.maxHeight = 0;
    this.imageHeight = 410;
    this.greyScale = false;
    this.flip = false;
    this.verticalLines = false;
    this.widthInfo = this.querySelector('.canvas__width span');
    this.heightInfo = this.querySelector('.canvas__height span');
    this.canvasContainer = this.querySelector('.canvas__container');
    this.canvasProductImage = this.querySelector('.canvas_product_image'); // Image to zoom
    this.selectionFrame = this.querySelector('.selection-frame'); // Reference to the selection frame
    this.scale = 1; // Initialize the scale for zooming

    this.elems.greyScale = this.querySelector('button[data-action="grayscale"]');
    this.elems.flip = this.querySelector('button[data-action="flip"]');
    this.elems.length = this.querySelector('button[data-action="length"]');
    this.elems.lengthLinesElem = this.querySelector('.length-lines');
    this.elems.zoomInButton = this.querySelector('#zoom-in');
    this.elems.zoomOutButton = this.querySelector('#zoom-out');

    this.dimensionsInput = this.querySelector(
      'input[name="properties[dimensions]"]'
    );
    this.greyscaleInput = this.querySelector(
      'input[name="properties[greyscale]"]'
    );
    this.customizerInput = this.querySelector(
      'input[name="properties[_customizer]"]'
    );

    this.elems.greyScale.addEventListener(
      'click',
      this.greyScaleImage.bind(this)
    );
    this.elems.flip.addEventListener('click', this.flipImage.bind(this));
    this.elems.length.addEventListener('click', this.showLengths.bind(this));
    this.elems.zoomInButton.addEventListener('click', this.zoomIn.bind(this));
    this.elems.zoomOutButton.addEventListener('click', this.zoomOut.bind(this));
  }

  connectedCallback() {
    const surface = Number(this.getAttribute('data-surface'));
    if (surface) {
      this.surface.m = surface;
      this.surface.ft = surface * 10.764;
      this.surface.cm = surface * 10000;
      this.surface.in = surface * 1550;
    }
    this.elems.form = this.querySelector('form');
    this.elems.idInput = this.querySelector('input[name=id]');
    this.elems.dialogElem = this.querySelector('dialog');
    this.elems.openButton = this.querySelector('[open-modal]');
    this.elems.cancelButtons = this.querySelectorAll('[close-modal]');
    this.elems.numberInputs = this.querySelectorAll('input[type=number]');
    this.elems.radioInputs = this.querySelectorAll('input[type=radio]');
    this.elems.quantityInput = this.querySelector('input[name=quantity]');
    this.elems.price = this.querySelector('.final-price');
    this.elems.buyButton = this.querySelector("#mural_cta")
    this.elems.buyButtonText = this.querySelector("#final-price-cta")
    this.elems.priceCompare = this.querySelector('.compare-final-price');
    this.elems.dimensions = this.querySelector('.total-surface');
    this.elems.rolls = this.querySelector('.rolls-quantity');
    this.elems.cminputs = this.querySelector(".form-surface");
    this.elems.ininputs = this.querySelector(".form-surface-feets");

    // Listeners
    this.elems.openButton.addEventListener('click', this.openDialog.bind(this));
    this.elems.cancelButtons.forEach((elem) => {
      elem.addEventListener('click', this.closeDialog.bind(this));
    });
    this.elems.numberInputs.forEach((input) => {
      input.addEventListener('input', this.onInputNumberChange.bind(this));
    });
    this.elems.radioInputs.forEach((input) => {
      if (input.checked) this.measure = input.value;
      input.addEventListener('change', this.onRadioChange.bind(this));
    });
    this.elems.form.addEventListener('submit', this.closeDialog.bind(this));
    this.pdfButton = this.querySelector('#downloadpdf');
    if (this.pdfButton) {
      this.pdfButton.addEventListener('click', this.generatePDF.bind(this));
    }
    this.extendSetup();
    this.update();
    this.convertToInches();
    this.unitConverter();
    this.showLengths(false); // This will update the lengths without toggling the lines

  }

  extendSetup() {
    this.calculateMaxSizes();
    new DragHorizontalScroll('.canvas__container');
    window.onresize = this.calculateMaxSizes.bind(this);
  }

  updateValues() {

    if (this.measure === "cm") {
      this.width = Number(this.elems.numberInputs[0].value);
      this.height = Number(this.elems.numberInputs[1].value);

      this.dimensions = Math.round(this.height * this.width * 100) / 100;
      this.totalQuantity = Math.ceil(this.dimensions / this.surface[this.measure]);
      this.elems.quantityInput.value = this.totalQuantity;

      const id = document.querySelector(
        'input[name="id"]:not([customizer-input])'
      ).value;

      document.querySelector(
        'input[name="quantity"]:not([customizer-input])'
      ).value = this.totalQuantity;

      this.elems.idInput.value = id;
      this.currentPrice = window.product.variants.find(
        (variant) => variant.id == id
      ).price;
      this.currentPriceCompare = window.product.variants.find(
        (variant) => variant.id == id
      ).compare_at_price
    } else if (this.measure === "in") {
      const widthFeet = Number(this.elems.numberInputs[2].value);
      const widthInches = Number(this.elems.numberInputs[3].value);
      const heightFeet = Number(this.elems.numberInputs[4].value);
      const heightInches = Number(this.elems.numberInputs[5].value);

      const widthTotalInches = (widthFeet * 12) + widthInches;
      const heightTotalInches = (heightFeet * 12) + heightInches;

      this.width = widthTotalInches;
      this.height = heightTotalInches;

      this.dimensions = Math.round(this.height * this.width * 100) / 100;
      this.totalQuantity = Math.ceil(this.dimensions / this.surface[this.measure]);
      this.elems.quantityInput.value = this.totalQuantity;

      const id = document.querySelector(
        'input[name="id"]:not([customizer-input])'
      ).value;

      document.querySelector(
        'input[name="quantity"]:not([customizer-input])'
      ).value = this.totalQuantity;

      this.elems.idInput.value = id;
      this.currentPrice = window.product.variants.find(
        (variant) => variant.id == id
      ).price;
      this.currentPriceCompare = window.product.variants.find(
        (variant) => variant.id == id
      ).compare_at_price
    }
    this.updateFrameSize(this.height, this.width);
  }

  updateUI() {
    this.dimensionsInput.value = `${this.elems.numberInputs[0].value}x${this.elems.numberInputs[1].value}${this.measure}`;

    const totalPrice = this.totalQuantity * (this.currentPrice / 100);


    if (this.measure === 'cm') {
      this.elems.dimensions.textContent =
        (this.dimensions * 0.0001).toFixed(2) + 'm²';
    } else if (this.measure === 'in') {
      this.elems.dimensions.textContent =
        (this.dimensions * 0.00694444).toFixed(2) + 'ft²';
    }
    console.log("window.Shopify.currency.active: ", window.Shopify)
    const currencyCode = window.Shopify.currency.active;
    const currencySymbol = new Intl.NumberFormat(undefined, { style: 'currency', currency: currencyCode })
      .formatToParts(1)
      .find(part => part.type === 'currency').value;

    console.log(currencySymbol); 

    this.elems.price.textContent = `${currencySymbol}${totalPrice.toFixed(2)}`;
    const totalPriceCompare = this.totalQuantity * (this.currentPriceCompare / 100)
    this.elems.priceCompare.textContent = `${currencySymbol}${totalPriceCompare.toFixed(2)}`;
    this.elems.buyButton.innerHTML = this.elems.buyButtonText.innerHTML;
    let discountPercentage = 0;
    if (totalPriceCompare > totalPrice) {
      discountPercentage = Math.round(((totalPriceCompare - totalPrice) / totalPriceCompare) * 100);
    }
    if (discountPercentage > 0) {
      const discountElement = document.querySelector(".discount-percentage");
      discountElement.textContent = `-${discountPercentage}%`;
    }
    console.log("totalPriceCompare yes: ", totalPriceCompare)

    this.widthInfo.textContent = `${this.elems.numberInputs[0].value}${this.measure}`;
    this.heightInfo.textContent = `${this.elems.numberInputs[1].value}${this.measure}`;

    this.updateFrameSize(this.height, this.width);
  }

  onInputNumberChange(e) {
    const max = Number(e.target.max);
    const min = Number(e.target.min);
    const val = Number(e.target.value);
    if (e.target.id === "width-inch" && e.target.value > 11) {
      this.elems.numberInputs[2].value = Number(this.elems.numberInputs[2].value) + 1;
      this.elems.numberInputs[3].value = 0;
    }
    if (e.target.id === "height-inch" && e.target.value > 11) {
      this.elems.numberInputs[4].value = Number(this.elems.numberInputs[4].value) + 1;
      this.elems.numberInputs[5].value = 0;
    }

    if (val > max) {
      e.target.value = max;
    }
    this.update();
  }

  onRadioChange(e) {
    this.measure = e.target.value;
    this.unitConverter();
    this.update();

    if (this.measure === "in") {
      this.elems.cminputs.style.display = "none";
      this.elems.ininputs.style.display = "block";
    } else if (this.measure === "cm") {
      this.elems.cminputs.style.display = "block";
      this.elems.ininputs.style.display = "none";
    }
  }

  unitConverter() {
    if (this.measure === "in") {
      const totalQuantity = Number(this.elems.quantityInput.value);
      const totalSurfaceInCm2 = totalQuantity * this.surface['cm'];

      const totalSurfaceInInches2 = totalSurfaceInCm2 * 0.155;
      this.dimensions = Math.round(totalSurfaceInInches2 * 100) / 100;

      let ratio = 1;
      let width = Math.sqrt(this.dimensions / ratio);
      let height = width * ratio;

      const maxInches = 780;

      if (width > maxInches) {
        width = maxInches;
        height = this.dimensions / maxInches;
      }

      if (height > maxInches) {
        height = maxInches;
        width = this.dimensions / maxInches;
      }

      const widthFeet = Math.floor(width / 12);
      const widthInches = Math.round(width % 12);
      const heightFeet = Math.floor(height / 12);
      const heightInches = Math.round(height % 12);

      this.elems.numberInputs[2].value = widthFeet;
      this.elems.numberInputs[3].value = widthInches;
      this.elems.numberInputs[4].value = heightFeet;
      this.elems.numberInputs[5].value = heightInches;

      this.width = width;
      this.height = height;

      this.totalQuantity = totalQuantity;

      const id = document.querySelector(
        'input[name="id"]:not([customizer-input])'
      ).value;

      document.querySelector(
        'input[name="quantity"]:not([customizer-input])'
      ).value = this.totalQuantity;

      this.elems.idInput.value = id;
      this.currentPrice = window.product.variants.find(
        (variant) => variant.id == id
      ).price;
      this.currentPriceCompare = window.product.variants.find(
        (variant) => variant.id == id
      ).compare_at_price
    } else if (this.measure === "cm") {
      const widthFeet = Number(this.elems.numberInputs[2].value);
      const widthInches = Number(this.elems.numberInputs[3].value);
      const heightFeet = Number(this.elems.numberInputs[4].value);
      const heightInches = Number(this.elems.numberInputs[5].value);

      const widthTotalInches = (widthFeet * 12) + widthInches;
      const heightTotalInches = (heightFeet * 12) + heightInches;

      this.width = widthTotalInches;
      this.height = heightTotalInches;

      const dimensionsInSquareFeet = (this.height * this.width) / 144;
      this.dimensions = Math.round(dimensionsInSquareFeet * 100) / 100;

      const totalSurfaceInCm2 = dimensionsInSquareFeet * 929.0304;

      let ratio = 1;
      let widthCm = Math.sqrt(totalSurfaceInCm2 / ratio);
      let heightCm = widthCm * ratio;

      this.elems.numberInputs[0].value = Math.round(widthCm);
      this.elems.numberInputs[1].value = Math.round(heightCm);

      this.width = widthCm;
      this.height = heightCm;

      this.totalQuantity = Math.ceil(totalSurfaceInCm2 / this.surface['cm']);

      const id = document.querySelector(
        'input[name="id"]:not([customizer-input])'
      ).value;

      document.querySelector(
        'input[name="quantity"]:not([customizer-input])'
      ).value = this.totalQuantity;

      this.elems.idInput.value = id;
      this.currentPrice = window.product.variants.find(
        (variant) => variant.id == id
      ).price;
      this.currentPriceCompare = window.product.variants.find(
        (variant) => variant.id == id
      ).compare_at_price
    }
  }

  update() {
    this.updateValues();
    this.updateUI();
    this.showLengths(false); // This will update the lengths without toggling the lines

  }

  updateFrameSize(height, width) {
    console.log("moved a little bit")
    // This method updates the selection frame size and position based on the height and width

    if (this.isReplicated) {
      this.canvasContainer = this.querySelector('.canvas__container')
      let widthPixels = 0
      let heightPixels = 0
      if (this.measure === 'cm') {
        widthPixels = parseFloat(width * this.pixels.cm)
        heightPixels = parseFloat(height * this.pixels.cm)
        if (widthPixels < 45 * this.pixels.cm) {
          widthPixels = 45 * this.pixels.cm
        }
        if (heightPixels < 100 * this.pixels.cm) {
          heightPixels = 100 * this.pixels.cm
        }
      }

      if (this.measure === 'in') {
        widthPixels = parseFloat(width * this.pixels.in)
        heightPixels = parseFloat(height * this.pixels.in)

        if (widthPixels < 17.7 * this.pixels.cm) {
          widthPixels = 17.7 * this.pixels.cm
        }
        if (heightPixels < 39.3 * this.pixels.cm) {
          heightPixels = 39.3 * this.pixels.cm
        }
      }

      const finalWidth = (widthPixels * this.imageHeight) / heightPixels
      let finalHeight = this.maxHeight

      if (finalWidth > this.maxWidth) {
        finalHeight = (this.maxWidth / finalWidth) * this.maxHeight
      }

      this.canvasContainer.style.height = finalHeight + 'px'
      this.canvasContainer.style.width = finalWidth + 'px'
    } else {
      const canvasImage = this.canvasContainer.querySelector('.canvas__image');
      const canvasWidth = canvasImage.clientWidth;
      const canvasHeight = canvasImage.clientHeight;

      let widthPixels = 0, heightPixels = 0;

      if (this.measure === 'cm') {
        widthPixels = width * this.pixels.cm;
        heightPixels = height * this.pixels.cm;
      } else if (this.measure === 'in') {
        widthPixels = width * this.pixels.in;
        heightPixels = height * this.pixels.in;
      }

      const inputAspectRatio = widthPixels / heightPixels;
      const canvasAspectRatio = canvasWidth / canvasHeight;

      let scaledWidth, scaledHeight;

      if (inputAspectRatio > canvasAspectRatio) {
        scaledWidth = Math.min(widthPixels, canvasWidth);
        scaledHeight = scaledWidth / inputAspectRatio;
      } else {
        scaledHeight = Math.min(heightPixels, canvasHeight);
        scaledWidth = scaledHeight * inputAspectRatio;
      }

      const existingFrame = this.selectionFrame;
      existingFrame.style.width = `${scaledWidth}px`;
      existingFrame.style.height = `${scaledHeight}px`;

      existingFrame.style.left = `${(canvasWidth - scaledWidth) / 2}px`;
      existingFrame.style.top = `${(canvasHeight - scaledHeight) / 2}px`;

      this.makeFrameDraggable();
    }

  }
  async captureFrameImage() {
    const productCustomizer = document.querySelector('product-customizer');
    if (!productCustomizer) {
      console.error('product-customizer not found.');
      return null;
    }

    const isReplicated = productCustomizer.getAttribute('replicate-product');
    const loadImage = (src) => {
      return new Promise((resolve, reject) => {
        const image = new Image();
        image.crossOrigin = 'anonymous';
        image.onload = () => resolve(image);
        image.onerror = (err) => reject(err);
        image.src = src;
      });
    };
    const canvasToBlob = (canvas, type = 'image/png') => {
      return new Promise((resolve, reject) => {
        canvas.toBlob((blob) => {
          blob ? resolve(blob) : reject(new Error('Canvas to blob conversion failed.'));
        }, type);
      });
    };

    try {
      if (!isReplicated) {
        const canvasContainer = document.querySelector('.canvas__image');
        const selectionFrame = canvasContainer?.querySelector('.selection-frame');
        const productImage = canvasContainer?.querySelector('.canvas_product_image');
        if (!canvasContainer || !selectionFrame || !productImage) {
          console.error("Required elements not found.");
          return null;
        }
        const imageRect = productImage.getBoundingClientRect();
        const frameRect = selectionFrame.getBoundingClientRect();
        const x = frameRect.left - imageRect.left;
        const y = frameRect.top - imageRect.top;
        const width = frameRect.width;
        const height = frameRect.height;
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = width;
        tempCanvas.height = height;
        const ctx = tempCanvas.getContext('2d');
        const bgUrl = getComputedStyle(productImage).backgroundImage.slice(5, -2);
        const image = await loadImage(bgUrl);
        ctx.drawImage(image, -x, -y, imageRect.width, imageRect.height);
        return await canvasToBlob(tempCanvas, 'image/png');
      } else {
        const containerEl = document.querySelector('.canvas__container');
        const backgroundEl = document.querySelector('.canvas_product_image');
        if (!containerEl || !backgroundEl) {
          console.error('Missing .canvas__container or .canvas_product_image');
          return null;
        }
        const containerRect = containerEl.getBoundingClientRect();
        const desiredWidth = Math.round(containerRect.width);
        const desiredHeight = Math.round(containerRect.height);
        if (desiredWidth <= 0 || desiredHeight <= 0) {
          console.error('Container has zero or negative dimensions');
          return null;
        }
        let bgUrl = getComputedStyle(backgroundEl).getPropertyValue('background-image');
        bgUrl = bgUrl?.replace(/^url\(['"]?/, '').replace(/['"]?\)$/, '');
        if (!bgUrl) {
          console.error('No valid background-image found');
          return null;
        }
        const offscreenCanvas = document.createElement('canvas');
        offscreenCanvas.width = desiredWidth;
        offscreenCanvas.height = desiredHeight;
        const ctx = offscreenCanvas.getContext('2d');
        const backgroundImage = await loadImage(bgUrl);
        const imgWidth = backgroundImage.width;
        const imgHeight = backgroundImage.height;
        const scale = desiredHeight / imgHeight;
        const scaledWidth = imgWidth * scale;
        const scaledHeight = desiredHeight;
        for (let x = 0; x < desiredWidth; x += scaledWidth) {
          ctx.drawImage(backgroundImage, x, 0, scaledWidth, scaledHeight);
        }
        return await canvasToBlob(offscreenCanvas, 'image/png');
      }
    } catch (error) {
      console.error('Error capturing frame image:', error);
      return null;
    }
  }

  makeFrameDraggable() {
    console.log("mkaeFrameDraggable is scrolling")
    const frame = this.selectionFrame;

    let isDragging = false;
    let startX = 0;
    let startY = 0;

    const startDragging = (e) => {
      isDragging = true;
      startX = (e.touches ? e.touches[0].clientX : e.clientX) - frame.offsetLeft;
      startY = (e.touches ? e.touches[0].clientY : e.clientY) - frame.offsetTop;
      frame.style.cursor = 'move';
      e.preventDefault();
    };

    const doDrag = (e) => {
      if (!isDragging) return;

      const currentX = (e.touches ? e.touches[0].clientX : e.clientX);
      const currentY = (e.touches ? e.touches[0].clientY : e.clientY);

      const newX = currentX - startX;
      const newY = currentY - startY;

      const maxX = this.canvasContainer.clientWidth - frame.offsetWidth;
      const maxY = this.canvasContainer.clientHeight - frame.offsetHeight;

      frame.style.left = `${Math.min(Math.max(newX, 0), maxX)}px`;
      frame.style.top = `${Math.min(Math.max(newY, 0), maxY)}px`;
    };

    const stopDragging = () => {
      isDragging = false;
      frame.style.cursor = 'default';
    };

    frame.addEventListener('mousedown', startDragging);
    document.addEventListener('mousemove', doDrag);
    document.addEventListener('mouseup', stopDragging);

    frame.addEventListener('touchstart', startDragging);
    document.addEventListener('touchmove', doDrag);
    document.addEventListener('touchend', stopDragging);
  }


  zoom(scaleChange) {
    console.log("scale change: ", scaleChange + " this.scale: ", this.scale);

    // Apply the scale change
    this.scale += scaleChange;

    // Ensure that the scale does not go below 1
    if (this.scale < 1) {
      this.scale = 1;
      console.log("reached the limit, scale set to 1");
    }

    // Cap the maximum scale at 2
    if (this.scale > 2) {
      this.scale = 2;
    }

    // Apply the scale transformation
    this.canvasProductImage.style.transform = `scale(${this.scale})`;
    this.canvasProductImage.style.transformOrigin = 'center';
  }

  zoomIn() {
    this.zoom(0.1);  // Zoom in by 10%
  }

  zoomOut() {
    this.zoom(-0.1);  // Zoom out by 10%
  }


  calculateMaxSizes() {
    if (screen.width < 820) {
      this.maxWidth = screen.width;
      this.maxHeight = screen.width;
    } else {
      this.maxWidth = 820;
      this.maxHeight = 410;
    }
    this.imageHeight = 410;
  }

  greyScaleImage() {
    this.greyScale = !this.greyScale;
    this.greyscaleInput.value = this.greyScale;
    if (this.greyScale) {
      this.elems.greyScale.classList.add('active');
      this.canvasContainer.style.filter = 'grayscale(1)';
    }

    if (!this.greyScale) {
      this.elems.greyScale.classList.remove('active');
      this.canvasContainer.style.filter = 'grayscale(0)';
    }
  }

  flipImage() {
    this.flip = !this.flip;

    if (this.flip) {
      this.elems.flip.classList.add('active');
      this.canvasProductImage.style.transform = 'scaleX(-1)';
    }

    if (!this.flip) {
      this.elems.flip.classList.remove('active');
      this.canvasProductImage.style.transform = 'scaleX(1)';
    }
  }

  showLengths(toggle = true) {
    // Only toggle `this.verticalLines` if `toggle` is true (i.e., no parameter or true is passed)
    if (toggle) {
      this.verticalLines = !this.verticalLines;
    }

    // Ensure `selectionFrame` is available
    if (!this.selectionFrame) {
      console.error('Selection frame not found');
      return;
    }

    // Clear any existing lines (both vertical lines and grid)
    this.selectionFrame.innerHTML = '';

    // If vertical lines are toggled on
    if (this.verticalLines) {
      this.elems.length.classList.add('active');

      const selectionFrameWidth = this.selectionFrame.clientWidth; // Get the width of the selection frame
      const selectedWidth = Number(document.getElementById('width').value); // Get the selected width in cm

      if (!selectedWidth || selectedWidth <= 0) {
        console.error('Invalid width selected.');
        return;
      }

      // Set the interval for the lines (e.g., every 50cm)
      const interval = 50;
      const numLines = Math.floor(selectedWidth / interval); // Calculate how many lines we need

      // Calculate the spacing between lines in the frame based on the width selected
      const sectionWidth = selectionFrameWidth / selectedWidth * interval;

      // Add vertical lines based on the width selected and interval
      for (let i = 1; i <= numLines; i++) {
        const line = document.createElement('div');
        line.classList.add('length-line');

        // Set the style for the vertical line
        line.style.position = 'absolute';
        line.style.left = `${i * sectionWidth}px`; // Position the line at the correct division
        line.style.top = '0';
        line.style.height = '100%';
        line.style.width = '1px';
        line.style.backgroundColor = 'black'; // Line color
        line.style.zIndex = '20'; // Ensure the line is on top of the selection frame content

        // Append the line to the selection frame
        this.selectionFrame.appendChild(line);
      }

    } else {
      // Add the default grid back when vertical lines are turned off
      this.elems.length.classList.remove('active');

      // Create grid cells (3x3 grid)
      for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
          const gridCell = document.createElement('div');
          gridCell.classList.add('grid-cell'); // Add a class for each grid cell

          // Set the style for the grid cell
          gridCell.style.border = '1px dashed black'; // Dashed grid lines
          gridCell.style.gridRowStart = row + 1;
          gridCell.style.gridColumnStart = col + 1;

          // Append the grid cell to the selection frame
          this.selectionFrame.appendChild(gridCell);
        }
      }
    }
  }






}
customElements.define('product-customizer', ProductCustomizer);


