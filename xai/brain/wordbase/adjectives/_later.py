

#calss header
class _LATER():
	def __init__(self,): 
		self.name = "LATER"
		self.definitions = [u'happening at a time in the future, or after the time you have mentioned: ', u"happening towards the end of a period of time or the end of someone's life: ", u'more modern or recent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
