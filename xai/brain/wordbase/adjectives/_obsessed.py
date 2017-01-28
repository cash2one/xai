

#calss header
class _OBSESSED():
	def __init__(self,): 
		self.name = "OBSESSED"
		self.definitions = [u'unable to stop thinking about something; too interested in or worried about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
