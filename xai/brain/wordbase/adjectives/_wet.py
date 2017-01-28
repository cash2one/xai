

#calss header
class _WET():
	def __init__(self,): 
		self.name = "WET"
		self.definitions = [u'covered in water or another liquid: ', u'Wet paint, ink, or a similar substance has not had time to dry and become hard: ', u'used to describe weather or periods of time when rain falls: ', u'to be completely wet: ', u'used to describe someone who has a weak character and does not express any forceful opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
