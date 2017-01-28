

#calss header
class _REMEDIAL():
	def __init__(self,): 
		self.name = "REMEDIAL"
		self.definitions = [u'A remedial action is intended to correct something that is wrong or to improve a bad situation: ', u"Remedial exercises are intended to improve someone's health when they are ill.", u'relating to teaching that is intended to help people who have difficulties in reading or writing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
