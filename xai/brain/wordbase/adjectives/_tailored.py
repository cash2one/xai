

#calss header
class _TAILORED():
	def __init__(self,): 
		self.name = "TAILORED"
		self.definitions = [u"used to describe a piece of clothing that is shaped to fit a person's body closely: ", u'used to describe clothing that is made for a particular person by a tailor', u'made or changed especially to be suitable for a particular situation or purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
