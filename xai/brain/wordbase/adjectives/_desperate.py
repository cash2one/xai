

#calss header
class _DESPERATE():
	def __init__(self,): 
		self.name = "DESPERATE"
		self.definitions = [u'very serious or bad: ', u'very great or extreme: ', u'needing or wanting something very much: ', u'feeling that you have no hope and are ready to do anything to change the bad situation you are in: ', u'willing to be violent, and therefore dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
