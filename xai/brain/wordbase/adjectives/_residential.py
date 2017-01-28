

#calss header
class _RESIDENTIAL():
	def __init__(self,): 
		self.name = "RESIDENTIAL"
		self.definitions = [u'A residential road, area, etc. has only private houses, not offices and factories.', u'A residential job, position, course, etc. is one for which you live at the same place where you work or study.', u'relating to where you live or have lived: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
